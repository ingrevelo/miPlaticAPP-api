from datetime import datetime
from pydantic import BaseModel
from db.user_db import get_user

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

database_movements = [
    MovementInDB(**{"id_movement": 0,
    "username": "cesarR12",
    "date": datetime(2020, 12, 19, 22, 44, 7, 670512),
    "movement": "income",
    "movement_type": "var",
    "movement_category": "transport",
    "description": "",
    "amount": 998184,
    "actual_balance": 10998184}),
    MovementInDB(**{"id_movement": 1,
    "username": "cesarR12",
    "date": datetime(2020, 12, 20, 22, 44, 7, 670537),
    "movement": "income",
    "movement_type": "var",
    "movement_category": "salary",
    "description": "",
    "amount": 422374,
    "actual_balance": 11420559}),
    MovementInDB(**{"id_movement": 2,
    "username": "cesarR12",
    "date": datetime(2020, 12, 20, 22, 44, 7, 670549),
    "movement": "outcome",
    "movement_type": "fix",
    "movement_category": "salary",
    "description": "",
    "amount": 432456,
    "actual_balance": 10988102}),
    MovementInDB(**{"id_movement": 3,
    "username": "cesarR12",
    "date": datetime(2020, 12, 21, 22, 44, 7, 670560),
    "movement": "outcome",
    "movement_type": "var",
    "movement_category": "home",
    "description": "",
    "amount": 601805,
    "actual_balance": 10386297}),
    MovementInDB(**{"id_movement": 4,
    "username": "cesarR12",
    "date": datetime(2020, 12, 21, 22, 44, 7, 670570),
    "movement": "outcome",
    "movement_type": "fix",
    "movement_category": "transport",
    "description": "",
    "amount": 336401,
    "actual_balance": 10049895}),
    MovementInDB(**{"id_movement": 5,
    "username": "cesarR12",
    "date": datetime(2020, 12, 21, 22, 44, 7, 670581),
    "movement": "outcome",
    "movement_type": "fix",
    "movement_category": "home",
    "description": "",
    "amount": 719941,
    "actual_balance": 9329953}),
    MovementInDB(**{"id_movement": 6,
    "username": "cesarR12",
    "date": datetime(2020, 12, 22, 22, 44, 7, 670593),
    "movement": "income",
    "movement_type": "var",
    "movement_category": "home",
    "description": "",
    "amount": 163178,
    "actual_balance": 9493132}),
    MovementInDB(**{"id_movement": 7,
    "username": "cesarR12",
    "date": datetime(2020, 12, 22, 22, 44, 7, 670603),
    "movement": "outcome",
    "movement_type": "var",
    "movement_category": "transport",
    "description": "",
    "amount": 68252,
    "actual_balance": 9424879}),
    MovementInDB(**{"id_movement": 8,
    "username": "cesarR12",
    "date": datetime(2020, 12, 22, 22, 44, 7, 670613),
    "movement": "outcome",
    "movement_type": "var",
    "movement_category": "transport",
    "description": "",
    "amount": 587960,
    "actual_balance": 8836919}),
    MovementInDB(**{"id_movement": 9,
    "username": "cesarR12",
    "date": datetime(2020, 12, 23, 22, 44, 7, 670622),
    "movement": "income",
    "movement_type": "fix",
    "movement_category": "home",
    "description": "",
    "amount": 606452,
    "actual_balance": 9443372})
]
generator = {"id":9}

def save_movement(movement_in_db: MovementInDB):
    generator["id"] = generator["id"] + 1
    movement_in_db.id_movement = generator["id"]
    database_movements.append(movement_in_db)
    return movement_in_db

"""
Modificado de acá hacia abajo
"""

def get_movement(query: MovementInDB):
    query = query.dict()
    movements = []
    data = database_movements
    if get_user(query['username']) == None:
        return None
    else:
        for key, value in query.items():
            if value == None:
                pass
            else:
                if key == 'dateFrom' or key == 'amountFrom':
                    if key == 'dateFrom':
                        key = 'date'
                        value = value.split("-")
                        value = datetime(int(value[0]),int(value[1]),int(value[2]))
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
                        value = value.split("-")
                        value = datetime(int(value[0]),int(value[1]),int(value[2]))
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



