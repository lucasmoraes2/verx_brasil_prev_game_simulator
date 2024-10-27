from fastapi import FastAPI

from app.config.database.database import engine
from app.models import models
from app.routes import game_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(game_routes.router)
