from core.gemini_client import ask_gemini


print("Connecting to Gemini...")

answer = ask_gemini(
    "Explain what an invoice is in one simple sentence."
)

print("\nGemini Response:")
print(answer)