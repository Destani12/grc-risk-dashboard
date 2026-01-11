# GRC Risk Dashboard

## What This Project Is
This project is a simple Governance, Risk, and Compliance (GRC) dashboard built using Python.

It takes security problems (called findings), connects them to security rules (called controls), and then calculates how risky each problem is for the business. The goal is to show which security issues should be fixed first.

This project is meant to show how cybersecurity problems turn into business risk and decision-making.

---

## Why I Built This
In cybersecurity, not every problem can be fixed at once. Companies need a way to decide:
- What is most dangerous?
- What affects the business the most?
- What should be fixed first?

This project simulates how GRC teams answer those questions using risk scoring and dashboards.

---

## What the Project Does
- Reads security findings from a file
- Maps each finding to a security control (based on NIST-style controls)
- Calculates **inherent risk** (risk before controls)
- Calculates **residual risk** (risk after controls are applied)
- Sorts risks from highest to lowest priority
- Displays the results in an executive-style dashboard

---

## Key GRC Concepts Used
- **Finding**: A security issue or problem that increases risk  
- **Control**: A rule or safeguard meant to reduce risk  
- **Inherent Risk**: Risk before any controls are applied  
- **Residual Risk**: Risk that remains after controls reduce it  
- **Risk Prioritization**: Deciding which problems to fix first based on impact

---

## Tools and Technologies
- Python
- Pandas (for data handling)
- Streamlit (for the dashboard)

---

## How to Run the Project
1. Install required libraries:
   ```bash
   pip install pandas streamlit
2. Run the dashboard
   ```bash
   streamlit run app/ui/dashboard.py
