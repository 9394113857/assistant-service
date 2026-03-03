class BaseIntentHandler:

    def handle(self, user_id: int, message: str) -> str:
        raise NotImplementedError("Handle method must be implemented.")