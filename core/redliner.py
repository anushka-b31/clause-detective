def run_rule_checks(contract_text):

    findings = []

    text = contract_text.lower()

    rules = {
        "governing law": {
            "risk": "Medium",
            "issue": "Missing Governing Law Clause"
        },
        "termination": {
            "risk": "Medium",
            "issue": "Missing Termination Clause"
        },
        "liability": {
            "risk": "High",
            "issue": "Missing Liability Clause"
        },
        "confidentiality": {
            "risk": "Medium",
            "issue": "Missing Confidentiality Clause"
        },
        "indemnification": {
            "risk": "High",
            "issue": "Missing Indemnification Clause"
        }
    }

    for keyword, data in rules.items():

        if keyword not in text:

            findings.append({
                "risk": data["risk"],
                "issue": data["issue"]
            })

    return findings
