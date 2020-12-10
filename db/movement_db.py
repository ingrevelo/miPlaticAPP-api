from datetime import datetime
from pydantic import BaseModel

class MovementInDB(BaseModel):
    id_movement: int = 0
    username: str
    date: datetime = datetime.now()
    movement: str # Income or Outcome
    movement_type: str # Fixed or Variable
    movement_category: str
    description: str
    amount: int
    actual_balance: int

database_movements = Dict[str, MovementInDB]

database_movements = {
    '10001': MovementInDB(**{
        'id_movement': 10001,
        'username': 'cesarR12',
        'date': datetime.datetime(2020, 12, 10, 17, 24, 36, 184761),
        'movement': 'income',
        'movement_type': 'fixed',
        'movement_category': 'salary',
        'description': 'monthly salary',
        'amount': 1000000,
        'actual_balance': 1000000
    }),

    '10002': MovementInDB(**{
        'id_movement': 10002,
        'username': 'cesarR12',
        'date': datetime.datetime(2020, 12, 10, 17, 30, 26, 277539),
        'movement': 'outcome',
        'movement_type': 'fixed',
        'movement_category': 'rent',
        'description': 'monthly rent',
        'amount': 250000,
        'actual_balance': 750000
    }),

    '10003': MovementInDB(**{
        'id_movement': 10003,
        'username': 'cesarR12',
        'date': datetime.datetime(2020, 12, 10, 17, 32, 29, 39614),
        'movement': 'outcome',
        'movement_type': 'fixed',
        'movement_category': 'transport',
        'description': 'monthly transport',
        'amount': 100000,
        'actual_balance': 650000
    }),

    '10004': MovementInDB(**{
        'id_movement': 10004,
        'username': 'cesarR12',
        'date': datetime.datetime(2020, 12, 10, 17, 36, 33, 261092),
        'movement': 'outcome',
        'movement_type': 'fixed',
        'movement_category': 'groceries',
        'description': 'monthly groceries',
        'amount': 100000,
        'actual_balance': 550000
    }),

    '10005': MovementInDB(**{
        'id_movement': 10005,
        'username': 'cesarR12',
        'date': datetime.datetime(2020, 12, 10, 17, 38, 8, 60232),
        'movement_type': 'outcome',
        'movement_category': 'restaurant',
        'description': '',
        'amount': 10000,
        'actual_balance': 540000
    })
}

generator = {'id':10005}

def save_movement(movement_in_db: MovementInDB):
    generator['id'] = generator['id'] + 1
    movement_in_db.id_movement = generator['id']
    database_movements.append(movement_in_db)
    return movement_in_db