from typing import Optional

from pydantic import BaseModel


class PlayerBase(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    position: str
    goals_scored: int
    squad_number: int
    wages: int
    games_played: int
    active: bool

    class Config:
        orm_mode = True