from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database.database import get_db
from app.controllers.game_controller import GameController

router = APIRouter(
    prefix="/jogo",
    tags=["game"]
)


@router.post("/simular")
def simulate_game(db: Session = Depends(get_db)):
    controller = GameController(db)
    return controller.simulate_game()
