import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
print(f"API Key: {API_KEY[:20]}...")

genai.configure(api_key=API_KEY)

print("\nAvailable models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"  - {m.name}")

# Try to use a model
try:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say hello")
    print(f"\n✓ gemini-pro works!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"\n✗ gemini-pro failed: {e}")
