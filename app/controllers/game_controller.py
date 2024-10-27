from sqlalchemy.orm import Session
from app.services.game_service import GameService

BEHAVIOR_TRANSLATION = {
    "impulsive": "impulsivo",
    "demanding": "exigente",
    "cautious": "cauteloso",
    "random": "aleatorio"
}


class GameController:
    def __init__(self, db: Session):
        self._db = db
        self._game_service = GameService(self._db)

    def simulate_game(self) -> dict:
        self._game_service.reset_game()

        result = self._game_service.start_game()

        vencedor_traduzido = BEHAVIOR_TRANSLATION.get(result["winner"], result["winner"])
        jogadores_traduzidos = [BEHAVIOR_TRANSLATION.get(behavior, behavior) for behavior in result["players"]]

        response_data = {
            "vencedor": vencedor_traduzido,
            "jogadores": jogadores_traduzidos
        }

        return response_data
