# AI Powered Support Ticket Classifier

## Overview

####  An automated support ticket classification system built using Flask, Google Gemini, Make.com, Tally Forms, ngrok, and Google Sheets.

#### The system receives customer complaints from a Tally form, sends them to a Flask API for processing, uses Google Gemini to classify the complaint, assign a priority level, generate a summary, and automatically routes the ticket to the appropriate Google Sheets workflow through Make.com.

## ❗ Problem It Solves

#### Businesses that handle customer complaints through forms often struggle with efficiently processing and organizing incoming support requests:

#### - Customer complaints arrive in unstructured formats from forms or emails
#### - Manual reading and categorization of tickets takes time and slows response
#### - Important issues may not be identified quickly enough
#### - Support teams lack a consistent system for prioritizing tickets
#### - No automated workflow to summarize and route tickets to the right place
#### - Data is often scattered across systems without structured tracking

This leads to delayed responses, poor prioritization, and inefficient support handling.

## 💡 Solution

#### This system automates the end-to-end customer support ticket processing workflow using AI, backend APIs, and no-code automation tools.

#### It processes incoming customer complaints submitted through a Tally form and:

#### - Sends the complaint data to a Flask API for structured processing
#### - Uses Google Gemini to analyze and classify the complaint into categories such as Billing, Technical, or Sales
#### - Assigns a priority level based on urgency and severity (e.g., payment issues are marked high priority)
#### - Generates a concise summary of the customer complaint for quick review
#### - Automatically routes the ticket into the appropriate Google Sheets workflow using Make.com based on classification and priority

#### This ensures faster response times, better ticket organization, and reduced manual effort for support teams.
## Screenshots

### Tally Form

![tally scr.png](Assets/tally%20scr.png)

### Make.com Workflow

![make.com scr.png](Assets/make.com%20scr.png)

### Google Sheets Output

![high priority.png](Assets/high%20priority.png)

![medium priority.png](Assets/medium%20priority.png)

![Low priority.png](Assets/Low%20priority.png)

## Features

* Complaint intake through Tally Forms
* Flask REST API
* Google Gemini integration
* AI-powered ticket classification
* Priority assignment
* AI-generated complaint summaries
* IST timestamp generation
* Make.com automation
* Google Sheets integration

## Tech Stack

* Python
* Flask
* Google Gemini 2.5 Flash
* Make.com
* Tally Forms
* Google Sheets
* ngrok

## Workflow

Tally Form

↓

Make.com Trigger

↓

HTTP Request

↓

Flask API

↓

Google Gemini

↓

Ticket Classification

↓

Priority Assignment

↓

Summary Generation

↓

Router

↓

Google Sheets

## Categories

The system classifies support tickets into:

* Technical
* Billing
* Sales

## Priority Levels

The system assigns one of the following priorities:

* High
* Medium
* Low

## Sample Input

```json
{
  "name": "John Doe",
  "email": "john@gmail.com",
  "complaint": "I cancelled my subscription but the payment was still processed."
}
```

## Sample Output

```json
{
  "name": "John Doe",
  "email": "john@gmail.com",
  "complaint": "I cancelled my subscription but the payment was still processed.",
  "category": "Billing",
  "priority": "High",
  "summary": "Customer reports payment being processed after cancellation.",
  "timestamp": "2026-06-12 15:45:12"
}
```

## Automation Flow

1. User submits a complaint through a Tally Form.
2. Make.com receives the submission through a webhook.
3. The complaint is sent to the Flask API.
4. Google Gemini analyzes the complaint.
5. Gemini returns:

   * Category
   * Priority
   * Summary
6. The API adds a timestamp.
7. Make.com routes the ticket.
8. Ticket data is stored in Google Sheets.


