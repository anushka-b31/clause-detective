import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_contract(contract_text):

    prompt = f"""
You are an expert legal contract reviewer.

Analyze the contract and provide the following sections:

# Contract Type
Identify whether the document is:
- NDA
- Employment Agreement
- Service Agreement
- Other

# Risky Clauses
List clauses that expose one party to significant legal or financial risk.

# Ambiguous Clauses
Identify unclear or vague wording.

# Missing Clauses
Identify important clauses that appear to be absent.

# Suggested Revisions
For each risky clause provide:

Original Clause:
[copy the clause from the contract]

Suggested Revision:
[improved clause]

Reason:
[why the change is recommended]

Contract:

{contract_text}
"""

    response = model.generate_content(prompt)

    return response.text
