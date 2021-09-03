from sqlalchemy.orm import Session

from . import models, schemas


def get_player(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()


def get_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Player).offset(skip).limit(limit).all()


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

