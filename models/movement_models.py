from pydantic import BaseModel
from datetime import datetime

class MovementIn(BaseModel):
    username: str
    movement: str
    movement_type: str
    movement_category: str
    description: str
    amount: int

class MovementOut(BaseModel):
    id_movement: int
    username: str
    date: datetime
    movement: str
    movement_type: str
    movement_category: str
    description: str
    amount: int
    actual_balance: int

"""
Modificado de acá hacia abajo
"""

class ConsultaIn(BaseModel):
    username: str
    movement: str = None
    movement_type: str = None
    movement_category: str = None
    dateFrom: str = None
    dateUntil: str = None
    amountFrom: int = None
    amountUntil: int = None

class ConsultaOut(BaseModel):
    query: list
