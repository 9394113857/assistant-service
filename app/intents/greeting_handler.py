# app/intents/greeting_handler.py

from datetime import datetime
from app.intents.base_handler import BaseIntentHandler


class GreetingHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:

        msg = message.lower().strip()

        current_hour = datetime.now().hour

        # 🌅 Time-based greeting
        if current_hour < 12:
            time_greeting = "Good morning ☀️"
        elif current_hour < 17:
            time_greeting = "Good afternoon 🌤"
        elif current_hour < 21:
            time_greeting = "Good evening 🌙"
        else:
            time_greeting = "Hello 🌟"

        # 👋 Basic greetings
        if any(word in msg for word in ["hi", "hello", "hey", "hii", "heyy"]):
            return f"{time_greeting}! 👋 How can I assist you today?"

        # 🙋 Asking assistant name
        if "your name" in msg:
            return "I'm your AI Assistant 🤖 here to help with products, orders, and recommendations."

        # 😊 Asking how are you
        if "how are you" in msg:
            return "I'm functioning perfectly! 🚀 How can I help you today?"

        # 👋 Thank you messages
        if any(word in msg for word in ["thank you", "thanks", "thx"]):
            return "You're welcome! 😊 Let me know if you need anything else."

        # 🌙 Good night
        if "good night" in msg:
            return "Good night! 🌙 Feel free to reach out anytime."

        # ☀ Good morning
        if "good morning" in msg:
            return "Good morning! ☀️ What would you like to explore today?"

        # 🌆 Good evening
        if "good evening" in msg:
            return "Good evening! 🌆 Need help with something?"

        # 🤝 Casual conversation starter
        if any(word in msg for word in ["what's up", "whats up", "sup"]):
            return "All set and ready to assist you! 🚀 What can I do for you?"

        # 🤖 Default fallback greeting
        return (
            f"{time_greeting}! 👋 "
            "I can help you with products, orders, or recommendations. "
            "What would you like to do?"
        )