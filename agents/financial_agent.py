from core.gemini_client import ask_gemini


def run_financial_audit(document_text):

    prompt = f"""
You are the Financial Auditor Agent of Agentic Auditor.

Your job is to audit the financial calculations in an invoice.

Analyze ONLY the information actually present in the document.

IMPORTANT RULES:

1. Calculate every line item independently:
   quantity × unit price

2. Calculate the subtotal independently:
   sum of all calculated line-item totals

3. Calculate the tax independently:
   subtotal × tax percentage

4. Calculate the final total independently:
   subtotal + tax

5. Compare your calculated values with the values stated in the invoice.

6. DO NOT report a mismatch when the calculated and stated values are equal.

7. Missing information is NOT automatically a mismatch.
   Mark it as INCOMPLETE instead.

8. Never invent numbers.

9. If all available calculations match:
   Financial Status MUST be VERIFIED.

10. If at least one stated numerical value differs from the independently
    calculated value:
   Financial Status MUST be MISMATCH.

11. If important financial information is missing and therefore cannot
    be verified:
   Financial Status MUST be INCOMPLETE.

Return exactly this structure:

FINANCIAL AUDIT

Financial Status: VERIFIED / MISMATCH / INCOMPLETE

Invoice Summary:
- Subtotal:
- Tax:
- Grand Total:

Calculation Check:
- Line Items:
- Subtotal Check:
- Tax Check:
- Grand Total Check:

Issues Found:

If there are no calculation errors, write:
"No calculation errors detected."

For every actual issue use:

1. [Issue]
   Severity: LOW / MEDIUM / HIGH
   Evidence: [Exact relevant information]
   Recommendation: [Recommended action]

Remember:
A missing invoice date, GSTIN, or other administrative information
is NOT a mathematical mismatch. Report it separately as an
incomplete-information issue.

Document:

{document_text}
"""

    return ask_gemini(prompt)