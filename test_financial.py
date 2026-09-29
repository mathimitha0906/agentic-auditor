from agents.financial_agent import run_financial_audit


document = """
INVOICE

Invoice Number: INV-1001

Seller:
ABC Software Solutions

Buyer:
XYZ Technologies

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

GST Amount: ₹10,800

Grand Total: ₹70,800

Payment Terms:
Payment due within 30 days.
"""


print("Starting Financial Auditor Agent...\n")

result = run_financial_audit(document)

print("========== FINANCIAL AUDIT ==========\n")
print(result)