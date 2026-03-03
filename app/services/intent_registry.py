from app.intents.product_handler import ProductHandler
from app.intents.order_handler import OrderHandler
from app.intents.recommendation_handler import RecommendationHandler
from app.intents.greeting_handler import GreetingHandler
from app.intents.unknown_handler import UnknownHandler


INTENT_HANDLER_MAP = {
    "product": ProductHandler,
    "order": OrderHandler,
    "recommendation": RecommendationHandler,
    "greeting": GreetingHandler,
    "unknown": UnknownHandler
}


def get_intent_handler(intent):
    handler_class = INTENT_HANDLER_MAP.get(intent, UnknownHandler)
    return handler_class()