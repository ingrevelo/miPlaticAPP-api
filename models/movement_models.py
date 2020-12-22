from pydantic import BaseModel
from datetime import datetime
from typing import List

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

class ConsultaIn(BaseModel):
    username: str = ''
    movement: str = ''
    movement_type: str = ''
    movement_category: str = ''
    dateFrom: str = ''
    dateUntil: str = ''
    amountFrom: int = ''
    amountUntil: int = ''

class ConsultaOut(BaseModel):
    consulta_dict: list