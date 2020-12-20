from datetime import datetime
import random
from matplotlib.pyplot import *

movement = ['income', 'outcome']
movement_type = ['fix', 'var']
movement_category = ['salary', 'education', 'home', 'transport']
database_movements = []
balance = 10000000
for i in range(100):
    move = random.choice(movement)
    amount = random.random()*1000000
    if move == 'income':
        balance = balance + amount
    else:
        balance = balance - amount
        
    movement_in_db = {
        'id_movement': i,
        'username': 'cesarR12',
        'date': datetime.now(),
        'movement': move,
        'movement_type': random.choice(movement_type),
        'movement_category': random.choice(movement_category),
        'description': '',
        'amount': amount,
        'actual_balance': balance
    }
    database_movements.append(movement_in_db)