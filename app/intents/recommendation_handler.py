from app.intents.base_handler import BaseIntentHandler
from app.services.tool_router import handle_recommendation_request


class RecommendationHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:
        return handle_recommendation_request(user_id)