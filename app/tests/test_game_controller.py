import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.database.database import Base
from app.controllers.game_controller import GameController
from app.repositories.player_repository import PlayerRepository
from app.repositories.property_repository import PropertyRepository

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        setup_test_data(db)
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


def setup_test_data(db):
    player_repo = PlayerRepository(db)
    property_repo = PropertyRepository(db)

    player_repo.create_player("Player 1", "impulsive")
    player_repo.create_player("Player 2", "demanding")
    player_repo.create_player("Player 3", "cautious")
    player_repo.create_player("Player 4", "random")

    for i in range(20):
        property_repo.create_property(cost=100 + i * 10, rent=20 + i * 5)

    db.commit()


def test_simulate_game(db):
    controller = GameController(db)

    response = controller.simulate_game()

    assert "vencedor" in response
    assert "jogadores" in response
    assert response["vencedor"] in ["impulsivo", "exigente", "cauteloso", "aleatorio"]
    assert all(player in ["impulsivo", "exigente", "cauteloso", "aleatorio"] for player in response["jogadores"])

