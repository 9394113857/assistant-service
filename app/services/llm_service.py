import os
import requests
from flask import current_app


OPENAI_URL = "https://api.openai.com/v1/chat/completions"


def generate_response(message: str) -> str:
    """
    Calls OpenAI API and returns assistant response.
    Falls back safely if API fails.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        current_app.logger.error("OPENAI_API_KEY not set.")
        return "AI service is not configured."

    try:
        response = requests.post(
            OPENAI_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are an intelligent ecommerce assistant. "
                            "You help users with products, orders, cart, and recommendations. "
                            "Keep answers concise and helpful."
                        )
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 300
            },
            timeout=20
        )

        if response.status_code != 200:
            current_app.logger.error(
                f"OpenAI API error: {response.status_code} - {response.text}"
            )
            return "AI service temporarily unavailable."

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"OpenAI request failed: {str(e)}")
        return "AI service connection failed."