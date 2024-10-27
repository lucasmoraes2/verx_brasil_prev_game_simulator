from sqlalchemy.orm import Session
from app.models import models


class PlayerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_players(self):
        return self.db.query(models.Player).all()

    def get_player_by_id(self, player_id: int):
        return self.db.query(models.Player).filter(models.Player.id == player_id).first()

    def update_balance(self, player_id: int, new_balance: int):
        player = self.get_player_by_id(player_id)
        if player:
            player.balance = new_balance
            self.db.commit()
            self.db.refresh(player)
        return player

    def create_player(self, name: str, behavior_type: str):
        new_player = models.Player(name=name, balance=300, behavior_type=behavior_type)
        self.db.add(new_player)
        self.db.commit()
        self.db.refresh(new_player)
        return new_player
