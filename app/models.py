from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, index=True)
    last_name = Column(String)
    position = Column(String)
    goals_scored = Column(Integer)
    squad_number = Column(Integer)
    active = Column(Boolean, default=True)
    wages = Column(Integer)
    games_played = Column(Integer)
