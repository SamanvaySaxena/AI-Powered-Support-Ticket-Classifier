# AI Support Ticket Classifier

## Overview

####  An automated support ticket classification system built using Flask, Google Gemini, Make.com, Tally Forms, ngrok, and Google Sheets.

#### The system receives customer complaints from a Tally form, sends them to a Flask API for processing, uses Google Gemini to classify the complaint, assign a priority level, generate a summary, and automatically routes the ticket to the appropriate Google Sheets workflow through Make.com.

## ❗ Problem It Solves

#### Businesses that receive customer support requests through forms or emails often face challenges in managing and prioritizing incoming issues:

#### - Support requests come in unstructured and mixed formats
#### - Important issues like billing problems or payment errors can get delayed
#### - Manual sorting of tickets into categories takes time and effort
#### - No clear system to decide which issues need immediate attention
#### - Business owners often waste time reviewing low-priority requests first
#### - Lack of structured tracking across different urgency levels

#### This leads to delayed responses, poor customer experience, and inefficient support handling.

## 💡 Solution

#### This system automates the classification and prioritization of customer support tickets using AI and workflow automation.

#### It processes incoming support requests from a Tally form, analyzes the customer's complaint, and then:

#### - Classifies tickets into categories such as Billing, Technical, or Sales
#### - Assigns a priority level based on urgency and issue severity
#### - High priority: billing issues, payment errors, double charges, urgent complaints
#### - Medium priority: general technical or service-related issues
#### - Low priority: non-urgent queries or informational requests
#### - Recommends a next action for the business owner:
#### - High priority → "Do a call"
#### - Medium priority → "Send an email"
#### - Low priority → "Archive request"
#### - Stores all processed tickets into separate spreadsheets based on priority level (High, Medium, Low)

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


