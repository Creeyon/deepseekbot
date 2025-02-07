import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")  # Ensure this environment variable is set correctly
if not api_key:
    raise ValueError("DEEPSEEK_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def get_deepseek_response(user_input):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "An unexpected error occurred. Please try again later."