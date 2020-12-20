from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.movement_db import MovementInDB
from db.movement_db import save_movement
from db.movement_db import get_movement
from models.user_models import UserIn, UserOut
from models.movement_models import MovementIn, MovementOut, ConsultaIn, ConsultaOut
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
    "https://miplaticaap-app.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get("/user/balance/{username}")
async def get_balance(username: str):

    user_in_db = get_user(username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out


@api.put("/user/movement/")
async def make_movement(movement_in: MovementIn):

    user_in_db = get_user(movement_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if movement_in.movement == 'outcome' and user_in_db.balance <= movement_in.amount: 
        raise HTTPException(status_code=400, detail="El gasto ingresado supera su balance actual de ahorro")

    if movement_in.movement == 'outcome':
        user_in_db.balance = user_in_db.balance - movement_in.amount
    else:
        user_in_db.balance = user_in_db.balance + movement_in.amount

    update_user(user_in_db)
    movement_in_db = MovementInDB(**movement_in.dict(), actual_balance = user_in_db.balance)
    movement_in_db = save_movement(movement_in_db)

    movement_out = MovementOut(**movement_in_db.dict())

    return  movement_out

"""
Modificado de acá hacia abajo
"""

@api.get("/user/consulta/")
async def get_consulta(consulta_in: ConsultaIn):

    consulta_in_db = get_movement(consulta_in)

    if consulta_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    # consulta_out = ConsultaOut(**consulta_in_db)

    return  consulta_in_db
