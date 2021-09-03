from . import crud
from .schemas import PlayerBase
from .player_list import player_list
from main import get_db

for player in player_list:
  player_in = PlayerBase(
    first_name=player["first_name"],
    last_name=player["last_name"],
    position=player["position"],
    goals_scored=player["goals_scored"],
    squad_number=player["squad_number"],
    wages=player["wages"],
    games_played=player["games_played"],
    active=player["active"]
  )
  crud.create_player(db=get_db(), player=player_in)