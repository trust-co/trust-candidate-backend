from sqlalchemy.orm import Session

from . import models, schemas


def create_player(db: Session, player: schemas.PlayerBase):
    db_player = models.Player(
      first_name=player.first_name,
      last_name=player.last_name,
      position=player.position,
      goals_scored=player.goals_scored,
      active=player.active,
      wages=player.wages,
      games_played=player.games_played,
      squad_number=player.squad_number
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

