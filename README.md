# NIDHI – Agentic AI Loan Assistant

🔗 Live Demo: (add Streamlit Cloud / local demo link if available)

---

## Overview

NIDHI is an **Agentic AI–driven personal loan assistant** designed for BFSI and NBFC use cases.  
It simulates an end-to-end digital loan journey — from conversational entry to sanction letter generation — using **governed, rule-based agent orchestration**.

The system prioritizes **explainability, compliance, and auditability**, making it suitable for regulated financial environments.

This prototype is built for **EY Techathon 6.0 – BFSI (Tata Capital)**.

---

## Key Features

- Conversational loan application via chatbot interface
- Master–Worker Agent orchestration model
- Rule-based credit & eligibility evaluation (BFSI-safe)
- Conditional document (salary slip) verification
- EMI affordability checks
- Automated loan sanction letter generation
- Transparent decision explanations
- Synthetic data & mocked integrations for demo safety

---

## Pages / UI Sections

- **Loan Assistant Chat**  
  Conversational interface controlled by the Master Agent

- **User Profile Panel**  
  Displays synthetic user details (income, PAN, credit score)

- **Loan Details Panel**  
  Loan amount selection, EMI estimates, interest rate

- **Application Status Panel**  
  Agent-wise progress tracking:
  - Verification Agent
  - Credit Evaluation Agent
  - Underwriting Agent
  - Sanction Agent

- **Document Upload Section**  
  Conditional salary slip upload for higher loan amounts

---

## Agent Roles & Responsibilities

- **Master Agent**
  - Controls conversation flow
  - Enforces policy & state transitions
  - Delegates tasks to worker agents

- **Verification Agent**
  - PAN and document validation
  - Conditional document requests

- **Underwriting Agent**
  - Credit score threshold checks
  - Pre-approved and 2× limit validation
  - EMI-to-income affordability logic

- **Sanction Agent**
  - Final approval processing
  - Sanction letter generation

All underwriting decisions are **deterministic and rule-based**.

---

## Decision Logic (Simplified)

- Credit Score ≥ 700 required
- Loan ≤ pre-approved limit → instant eligibility
- Loan ≤ 2× pre-approved limit → salary slip required
- EMI must be ≤ 50% of monthly income
- Otherwise → rejection with explanation

No LLM is used for credit decisioning.

---

## API Endpoints (Logical – Internal)

> This prototype uses internal functions instead of exposed APIs.

- Loan request processing (Underwriting Agent)
- Document verification simulation
- EMI calculation
- Sanction letter generation

These are designed to be replaceable with real NBFC APIs.

---

## Tech Stack

- **Frontend & UI**: Streamlit
- **Backend Logic**: Python
- **Agent Orchestration**: Rule-based workflow
- **State Management**: Streamlit Session State
- **Data**: Synthetic user & credit data
- **Deployment Ready**: Streamlit Cloud / Cloud VM

---

## User Workflow (Text)

1. User starts a conversation requesting a loan
2. Master Agent captures intent and routes the flow
3. Credit score is evaluated
4. Loan amount is checked against policy limits
5. Salary slip is requested if required
6. EMI affordability is validated
7. Loan is approved or rejected with explanation
8. Sanction letter is generated on approval

---

## Demo Notes

- All data used is **synthetic**
- External credit bureaus and CRM systems are **mocked**
- Designed to demonstrate **governance-first agent orchestration**
- Underwriting is intentionally non-LLM for BFSI compliance

---

## Credits

Built by **Team VibeGlitch**  
EY Techathon 6.0 – BFSI Track

- Dhrubaparna Mazumder  
- Mainakee Paul
