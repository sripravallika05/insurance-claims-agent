# Autonomous Insurance Claims Processing Agent

AI-powered backend system for processing insurance claim PDFs using FastAPI, document extraction, validation, and automated routing workflows.

---

# Features

- Upload insurance claim PDFs
- Extract structured claim information
- Detect missing mandatory fields
- Automated claim routing engine
- Fraud keyword detection
- FastAPI backend APIs
- Swagger API documentation

---

# Tech Stack

## Backend
- FastAPI
- Python
- Uvicorn

## PDF Processing
- pdfplumber
- Regex extraction

## API Testing
- Swagger UI

---

# Project Workflow

```text
PDF Upload
   ↓
PDF Text Extraction
   ↓
Field Extraction
   ↓
Validation Engine
   ↓
Routing Logic
   ↓
JSON Response
```

---

# Project Structure

```text
insurance-claims-agent/
│
├── app/
│   ├── main.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── services/
│   │   ├── pdf_extractor.py
│   │   ├── field_extractor.py
│   │   ├── validator.py
│   │   ├── router.py
│   │   └── reasoning.py
│   │
│   └── uploads/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/autonomous-insurance-claims-agent.git
```

## Navigate To Project

```bash
cd autonomous-insurance-claims-agent
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python -m uvicorn app.main:app --reload
```

---

# API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## Process Claim PDF

```http
POST /process-claim
```

### Input
- Insurance claim PDF

### Output

```json
{
  "extractedFields": {
    "policy_number": "ABC123",
    "incident_date": "05/10/2026",
    "estimated_damage": "12000"
  },
  "missingFields": [],
  "recommendedRoute": "Fast-track",
  "reasoning": "Estimated damage is below 25,000."
}
```

---

# Claim Routing Logic

| Condition | Route |
|---|---|
| Missing fields | Manual Review |
| Fraud keywords detected | Investigation Flag |
| Injury claims | Specialist Queue |
| Damage < 25,000 | Fast-track |
| Otherwise | Standard Review |

---

# Future Improvements

- AI/LLM-based field extraction
- OCR support for scanned PDFs
- Database integration
- React frontend dashboard
- Docker deployment
- Cloud deployment
- Real-time fraud scoring

---

# Screenshots

## Swagger UI

_Add screenshots here_
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/f3126d48-3832-4af3-8a28-02f853feb335" />


# Learning Outcomes

This project demonstrates:

- Backend API development
- PDF document processing
- Workflow automation
- Rule engine implementation
- Validation systems
- AI workflow design
- File upload handling

---

# Author
Sri Pravallika Malla

