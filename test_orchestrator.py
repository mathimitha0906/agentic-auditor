from core.orchestrator import run_full_audit


document = """
SOFTWARE DEVELOPMENT AGREEMENT

This agreement is between ABC Technologies and John Solutions.

John Solutions will provide software development services.

The software will be delivered after completion of development.

Either party may terminate this agreement.

The client will pay ₹50,000 for the services.
The payment will be made within 30 days.

Both parties agree to keep confidential information private.


INVOICE

Item 1:
Software Development
Quantity: 2
Unit Price: ₹25,000

Item 2:
Testing Services
Quantity: 1
Unit Price: ₹10,000

Subtotal: ₹60,000
GST: 18%
Tax: ₹10,800
Grand Total: ₹70,800
"""


print("========================================")
print("       AGENTIC AUDITOR")
print("     MULTI-AGENT AUDIT TEST")
print("========================================")


result = run_full_audit(document)


print("\n\n========================================")
print("       FINAL AUDIT REPORT")
print("========================================")


print("\n\n🛡️ COMPLIANCE AUDIT")
print("----------------------------------------")
print(result["compliance"])


print("\n\n💰 FINANCIAL AUDIT")
print("----------------------------------------")
print(result["financial"])


print("\n\n💬 CLIENT COMMUNICATION")
print("----------------------------------------")
print(result["communication"])


print("\n\n========================================")
print("       AUDIT COMPLETED")
print("========================================")