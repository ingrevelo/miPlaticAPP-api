from datetime import datetime
from pydantic import BaseModel

class MovementInDB(BaseModel):
    id_movement: int = 0
    username: str
    date: datetime = datetime.now()
    movement: str
    movement_type: str
    movement_category: str
    description: str
    amount: int
    actual_balance: int

database_movements = []
generator = {"id":0}

def save_movement(movement_in_db: MovementInDB):
    generator["id"] = generator["id"] + 1
    movement_in_db.id_movement = generator["id"]
    database_movements.append(movement_in_db)
    return movement_in_db

"""
Modificado de acá hacia abajo
"""

def get_movement(query: MovementInDB):
    query = query.dict()['query']
    movements = []
    data = database_movements
    for key, value in query.items():
        if key == 'dateFrom' or key == 'amountFrom':
            if key == 'dateFrom':
                key = 'date'
                value = datetime(value[0],value[1],value[2])
            elif key == 'amountFrom':
                key = 'amount'
            for move in data:
                if move.dict()[key] >= value:
                    movements.append(move)
            data = movements
            movements = []
        elif key == 'dateUntil' or key == 'amountUntil':
            if key == 'dateUntil':
                key = 'date'
                value = datetime(value[0],value[1],value[2])
            elif key == 'amountUntil':
                key = 'amount'
            for move in data:
                if move.dict()[key] <= value:
                    movements.append(move)
            data = movements
            movements = []
        else:
            for move in data:
                if move.dict()[key] == value:
                    movements.append(move)
            data = movements
            movements = []

                
    return data



