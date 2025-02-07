import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

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