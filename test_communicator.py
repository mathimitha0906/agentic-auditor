from agents.communicator_agent import run_client_communication


compliance_result = """
Overall Risk: HIGH

Issues Found:
1. Missing Intellectual Property clause
2. Ambiguous Scope of Services
3. Ambiguous Delivery Terms
"""


financial_result = """
Financial Status: VERIFIED

Subtotal: ₹60,000
Tax: ₹10,800
Grand Total: ₹70,800

No calculation errors detected.
"""


print("Starting Client Communicator Agent...")

result = run_client_communication(
    compliance_result,
    financial_result
)

print("\n========== CLIENT COMMUNICATION ==========\n")
print(result)