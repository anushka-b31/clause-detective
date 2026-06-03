Clause Detective

AI-Powered Contract Review Platform
Clause Detective helps users analyze contracts, identify legal risks, detect missing clauses, and receive AI-generated recommendations for improving contract language.

Overview
Reviewing contracts manually is time-consuming and often requires legal expertise. Clause Detective uses AI to assist users by highlighting potential risks, identifying ambiguous language, detecting missing provisions, and suggesting improvements.

Features
- Contract PDF Upload
- AI-Powered Contract Analysis
- Risk Assessment
- Missing Clause Detection
- Ambiguous Clause Identification
- Contract Health Score
- Rule-Based Legal Checks
- AI Recommendations for Improvement

Tech Stack
Frontend
- Streamlit

Backend
- Python

AI Model
- Google Gemini 1.5 Flash

PDF Processing
- pdfplumber


Project Structure
clause-detective/
│
├── app.py
│
├── core/
│   ├── parser.py
│   ├── analyzer.py
│   ├── risk_rules.py
│   └── redliner.py
├── .env
└── README.md


How It Works
1. Upload a contract PDF.
2. Extract contract text using pdfplumber.
3. Analyze the contract using Gemini AI.
4. Detect risky, ambiguous, and missing clauses.
5. Generate recommendations and risk insights.
6. Display findings through an interactive dashboard.


Future Enhancements
- Automated clause redlining
- DOCX support
- PDF report generation
- Contract comparison
- Compliance checking
- Multi-language support
