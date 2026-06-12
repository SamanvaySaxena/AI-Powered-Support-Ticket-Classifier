import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import datetime
import pytz

# Load .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment
API_KEY = os.getenv("GOOGLE_API_KEY")

# Safety check (VERY IMPORTANT)
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Use model from YOUR account
MODEL = "gemini-2.5-flash"




@app.route("/")
def home():
    return "AI Support Ticket Classifier Running"


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    name = data.get("name",'Anonymous')
    email = data.get("email",'No email provided')

    complaint = data.get("complaint", "No complaint provided")

    if not complaint:
        return jsonify({"error": "No complaint provided"}), 400



    ist = pytz.timezone("Asia/Kolkata")
    timestamp = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    url = f"https://generativelanguage.googleapis.com/v1/models/{MODEL}:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text" : f"""
You are an AI support ticket classifier used in a customer support automation system.

Your job is to analyze a customer complaint and return structured, consistent output.

---

### CLASSIFICATION TASK
Classify the complaint into exactly ONE category:

Categories:
- Technical: bugs, errors, login issues, app not working, performance issues, system failure
- Billing: payment issues, refunds, double charges, subscription problems, invoice issues
- Sales: pricing questions, plan upgrades, purchase interest, discounts

---

### PRIORITY RULES
Also assign priority based on severity:

HIGH:
- payment issues, refund requests, account locked, login failure, system not working

MEDIUM:
- feature not working properly, delays, bugs that don’t block usage

LOW:
- general questions, pricing inquiries, feature requests, sales questions

---

### OUTPUT RULES (VERY IMPORTANT)
- Return ONLY valid JSON
- No explanations
- No extra text
- No markdown

---

### OUTPUT FORMAT
{{
  "category": "Technical | Billing | Sales",
  "priority": "High | Medium | Low",
  "summary": "short 1-line summary of the complaint"
}}

---

### COMPLAINT
{complaint}
"""
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)
    result = response.json()

    try:
        raw_text = result["candidates"][0]["content"]["parts"][0]["text"]

        import json
        parsed = json.loads(raw_text)

        category = parsed.get("category", "Unknown")
        priority = parsed.get("priority", "priority not allotted")
        summary = parsed.get("summary", "summary unavailable")
    except Exception:
        return jsonify({
            "error": "Gemini response failed",
            "details": result
        }), 500


    return jsonify({
        "name": name,
        "email": email,
        "complaint": complaint,
        "category": category,
        "priority": priority,
        "summary": summary,
        "timestamp": timestamp
    })


if __name__ == "__main__":
    app.run(debug=True,port=5000)