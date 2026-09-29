import json

from core.gemini_client import ask_gemini


def run_compliance_audit(document_text):

    prompt = f"""
You are the Compliance Officer Agent inside an AI document auditing system.

Your task is to analyze the following business document.

Identify:
1. Potential compliance or contractual risks
2. Missing important clauses
3. Ambiguous clauses
4. Clauses that require human review
5. Recommended actions

IMPORTANT:
- Do not claim that something is definitely illegal unless the document clearly establishes that.
- Clearly distinguish potential risks from confirmed facts.
- Do not invent information that is not present in the document.

Return the result in this format:

COMPLIANCE AUDIT

Overall Risk: LOW / MEDIUM / HIGH

Issues Found:
1. [Issue]
   Severity: LOW / MEDIUM / HIGH
   Evidence: [Relevant document wording]
   Recommendation: [Action]

2. [Issue]
   Severity: LOW / MEDIUM / HIGH
   Evidence: [Relevant document wording]
   Recommendation: [Action]

Document:

{document_text}
"""

    return ask_gemini(prompt)