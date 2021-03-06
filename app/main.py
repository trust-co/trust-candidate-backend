from typing import List

from fastapi import Depends, FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .player_list import player_list

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/players", response_model=List[schemas.PlayerBase])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players


# Generate all players from a fixture
# Only allowed to be used once
@app.get("/generate-players", status_code=200)
def generate_players(db: Session = Depends(get_db)):
    existing_players = crud.get_players(db)
    if len(existing_players) > 0:
        raise HTTPException(
            status_code=422, detail="Squad already generated.")

    for player in player_list:
        player_in = schemas.PlayerBase(
        first_name=player["first_name"],
        last_name=player["last_name"],
        position=player["position"],
        goals_scored=player["goals_scored"],
        squad_number=player["squad_number"],
        wages=player["wages"],
        games_played=player["games_played"],
        active=player["active"]
    )
        crud.create_player(db=db, player=player_in)
