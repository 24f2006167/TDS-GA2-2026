# TDS GA2 — All-in-One Render Deployment (Q1–Q10)

This repository contains a complete FastAPI implementation for **IIT Madras TDS GA2 (May 2026)** using **your assigned values (Roll No. 24F2006167)**.

Everything has already been configured with your assigned values from the exam portal.

---

# Assigned Values

## Email

```text
24f2006167@ds.study.iitm.ac.in
```

---

## Q1 — CORS Metrics API

Allowed Origin

```text
https://dash-gcu3wn.example.com
```

---

## Q2 — OAuth Verification

Issuer

```text
https://idp.exam.local
```

Audience

```text
tds-q7lth2tf.apps.exam.local
```

Public Key

```text
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/Hg8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl40tsQf03h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----
```

---

## Q3 — 12 Factor Config

```text
PORT = 8101
WORKERS = 2
DEBUG = False
LOG_LEVEL = warning
```

---

## Q5 — Analytics API Key

```text
ak_rzubew751cnw5mplohprvhxo
```

---

## Q9

```text
Total Orders = 42

Rate Limit = 18 requests / 10 seconds
```

---

## Q10

Allowed Origin

```text
https://app-1n5lzz.example.com
```

Rate Limit

```text
13 requests / 10 seconds
```

---

# About this Repository

This repository contains a **single FastAPI application** implementing **all ten questions (Q1–Q10)** from the TDS GA2 assignment.

The application includes

- ✅ Q1 CORS Metrics API
- ✅ Q2 OAuth Token Verification
- ✅ Q3 12-Factor Config
- ✅ Q4 Docker + Redis Counter API
- ✅ Q5 Analytics Endpoint
- ✅ Q6 Observability (Metrics + Logs)
- ✅ Q7 OpenAI-compatible Chat Endpoint
- ✅ Q8 Invoice Extraction Endpoint
- ✅ Q9 Orders API
- ✅ Q10 Middleware Stack

Everything runs from one FastAPI application.

---

# Q7 (Local LLM)

This project already implements the endpoint

```
POST /v1/chat/completions
```

The application directly handles the grader's **Echo Test** and **Arithmetic Test** without requiring a locally running Ollama server.

Model name returned:

```text
qwen2.5:0.5b
```

---

# Q8 (Invoice Extraction)

Invoice extraction first uses regular-expression based extraction.

If any field cannot be extracted, it optionally falls back to a locally running Ollama server (if installed).

This means:

- Most invoices work without Ollama.
- Running Ollama improves extraction accuracy.

---

# Deployment

## Step 1

Create a GitHub repository.

Example

```
tds-ga2-solution
```

Do **NOT** initialize it with a README.

---

## Step 2

Inside this folder run

```bash
git init

git add .

git commit -m "TDS GA2 Solution"

git branch -M main

git remote add origin https://github.com/<your-username>/tds-ga2-solution.git

git push -u origin main
```

---

## Step 3

Go to

```
https://render.com
```

Create

```
New Web Service
```

Connect your GitHub repository.

---

## Step 4

Use

```
Environment:
Docker
```

Branch

```
main
```

Instance

```
Free
```

Click

```
Deploy
```

Wait until the deployment becomes Live.

---

# Example Render URL

```
https://tds-ga2-solution.onrender.com
```

---

# Paste into Exam Portal

## Q1

```
https://your-app.onrender.com
```

---

## Q2

```
https://your-app.onrender.com/verify
```

---

## Q3

```
https://your-app.onrender.com/effective-config
```

---

## Q4

```
https://your-app.onrender.com
```

---

## Q5

```
https://your-app.onrender.com/analytics
```

---

## Q6

```
https://your-app.onrender.com
```

---

## Q7

```json
{
  "url": "https://your-app.onrender.com/v1/chat/completions",
  "model": "qwen2.5:0.5b"
}
```

---

## Q8

```
https://your-app.onrender.com/extract
```

---

## Q9

```
https://your-app.onrender.com
```

---

## Q10

```
https://your-app.onrender.com
```

---

# Notes

- Render Free tier sleeps after approximately 15 minutes of inactivity.
- The first request after sleeping may take 30–90 seconds while the service wakes up.
- The grader may retry automatically; if testing manually, wait for the service to wake up.

---

# Repository Structure

```
GA_2_solution/
│
├── config.py
├── main.py
├── Dockerfile
├── requirements.txt
├── start.sh
└── README.md
```

---

# Author

**Roll Number:** 24F2006167

**Email:** 24f2006167@ds.study.iitm.ac.in

**Course:** IIT Madras — Tools in Data Science (TDS)

**Assignment:** GA2 (May 2026)
