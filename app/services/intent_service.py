from app.intents.base_handler import BaseIntentHandler
from app.services.tool_router import handle_recommendation_request


class RecommendationHandler(BaseIntentHandler):

    def handle(self, user_id: int, message: str) -> str:

        # User must be logged in for recommendations
        if not user_id:
            return "Please login to access personalized recommendations."

        # Call recommendation service
        return handle_recommendation_request(user_id)