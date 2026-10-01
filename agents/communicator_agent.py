from core.gemini_client import ask_gemini


def run_communication_audit(audit_context):
    """
    Converts compliance, financial, and cross-document
    findings into a clear business-friendly summary.
    """

    prompt = f"""
You are the Client Communicator Agent in an AI-powered
business auditing system called Agentic Auditor.

Your job is to convert technical audit findings into a
clear, professional business summary.

IMPORTANT RULES:

1. Do not invent facts.
2. Clearly distinguish contract information from invoice information.
3. If the contract amount and invoice amount differ, explicitly mention
   the difference.
4. Do not call an amount an error if the arithmetic itself is correct.
5. Explain the business impact clearly.
6. Give practical recommended actions.
7. Keep the output structured and easy to understand.
8. This is an AI-generated informational audit, not professional
   legal or financial advice.

AUDIT DATA:

{audit_context}

Return the following format:

CLIENT AUDIT SUMMARY

Overall Assessment:
[Short overall assessment]

Cross-Document Findings:
[List important contract vs invoice differences]

Compliance Findings:
[List important compliance issues]

Financial Findings:
[List important financial findings]

Recommended Actions:
1. [Action]
2. [Action]
3. [Action]

Business Impact:
[Explain the possible business impact]

Next Steps:
[Explain what the user should review or clarify]

Disclaimer:
This AI-generated audit summary is for informational purposes
and should be reviewed by an appropriate professional before
making legal or financial decisions.
"""

    return ask_gemini(prompt)


# Compatibility alias
def run_communicator(audit_context):
    return run_communication_audit(audit_context)