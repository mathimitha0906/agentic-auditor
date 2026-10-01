from agents.compliance_agent import run_compliance_audit
from agents.financial_agent import run_financial_audit
from agents.communicator_agent import run_communication_audit


def run_full_audit(contract_text, invoice_text):
    """
    Runs the complete Agentic Auditor workflow.

    Contract and invoice are analyzed separately first.
    Then the Client Communicator receives both results
    and creates a unified business summary.
    """

    # ======================================================
    # 1. COMPLIANCE AGENT
    # ======================================================

    combined_contract_context = f"""
DOCUMENT TYPE: SERVICE AGREEMENT

{contract_text}
"""

    compliance_result = run_compliance_audit(
        combined_contract_context
    )

    # ======================================================
    # 2. FINANCIAL AGENT
    # ======================================================

    invoice_context = f"""
DOCUMENT TYPE: INVOICE

{invoice_text}

IMPORTANT:
This is an invoice document.

Do not treat contract payment terms as invoice
calculations.

Only verify:
- line items
- quantities
- unit prices
- subtotal
- tax
- grand total
- arithmetic consistency
"""

    financial_result = run_financial_audit(
        invoice_context
    )

    # ======================================================
    # 3. CROSS-DOCUMENT COMPARISON
    # ======================================================

    comparison = f"""
CONTRACT:

{contract_text}


INVOICE:

{invoice_text}


COMPLIANCE ANALYSIS:

{compliance_result}


FINANCIAL ANALYSIS:

{financial_result}
"""

    # ======================================================
    # 4. CLIENT COMMUNICATOR
    # ======================================================

    communication_result = run_communication_audit(
        comparison
    )

    # ======================================================
    # FINAL RESULT
    # ======================================================

    return {
        "compliance": compliance_result,
        "financial": financial_result,
        "communication": communication_result,
    }