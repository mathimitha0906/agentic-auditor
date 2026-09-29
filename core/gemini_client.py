import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

client = genai.Client(api_key=API_KEY)

# Fast, cost-efficient model for our development/testing
MODEL_NAME = "gemini-3.5-flash-lite"


def ask_gemini(prompt):
    """Send a prompt to Gemini and return the response."""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text