from app.repositories.player_repository import PlayerRepository
from app.repositories.property_repository import PropertyRepository
from app.behaviors.player_behavior import (
    ImpulsiveBehavior,
    DemandingBehavior,
    CautiousBehavior,
    RandomBehavior
)
import random
from sqlalchemy.orm import Session


class GameService:
    def __init__(self, db: Session):
        self._players = []
        self._max_rounds = 1000
        self._round = 0
        self._num_properties = 20
        self._db: Session = db
        self._player_repository = PlayerRepository(db)
        self._property_repository = PropertyRepository(db)

    def _get_behavior(self, behavior_type):
        if behavior_type == "impulsive":
            return ImpulsiveBehavior()
        elif behavior_type == "demanding":
            return DemandingBehavior()
        elif behavior_type == "cautious":
            return CautiousBehavior()
        elif behavior_type == "random":
            return RandomBehavior()
        else:
            raise ValueError(f"Unknown behavior type: {behavior_type}")

    def reset_game(self):
        initial_balance = 300
        players = self._player_repository.get_all_players()
        for player in players:
            player.balance = initial_balance
            player.position = 0
            self._db.commit()

        properties = self._property_repository.get_all_properties()
        for property in properties:
            property.owner_id = None
            self._db.commit()

    def start_game(self):
        self._players = self._player_repository.get_all_players()

        for player in self._players:
            player.position = 0
            player.behavior = self._get_behavior(player.behavior_type)

        if not self._players:
            return {"error": "No players available in the database."}

        while len(self._players) > 1 and self._round < self._max_rounds:
            self._play_round()
            self._round += 1

        winner = max(self._players, key=lambda p: p.balance)
        return {
            "winner": winner.behavior_type,
            "players": sorted(
                [p.behavior_type for p in self._players],
                key=lambda behavior: [p.balance for p in self._players if p.behavior_type == behavior],
                reverse=True,
            ),
        }

    def _play_round(self):
        properties = self._property_repository.get_all_properties()
        for player in self._players:
            roll = random.randint(1, 6)

            previous_position = player.position
            player.position = (player.position + roll) % self._num_properties

            if player.position < previous_position:
                player.balance += 100

            property_id = player.position
            property = self._property_repository.get_property_by_id(property_id)

            if property is None:
                continue

            if property.owner_id is None:
                if player.behavior.should_buy_property(player, property):
                    self._buy_property(player, property)
            else:
                self._pay_rent(player, property)

    def _buy_property(self, player, property):
        if player.balance >= property.cost:
            player.balance -= property.cost
            self._property_repository.update_owner(property.id, player.id)

    def _pay_rent(self, player, property):
        rent = property.rent
        if player.balance >= rent:
            player.balance -= rent
            owner_id = property.owner_id
            owner = self._player_repository.get_player_by_id(owner_id)
            if owner:
                owner.balance += rent
                self._player_repository.update_balance(owner.id, owner.balance)
