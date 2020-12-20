from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

database_users = Dict[str, UserInDB]

database_users = {
    "cesarR12": UserInDB(**{"username":"cesarR12",
                            "password":"g2m1e5-R12",
                            "balance":10000000}),

    "carlosG19": UserInDB(**{"username":"carlosG19",
                            "password":"g2m1e5-G19",
                            "balance":1000000}),

    "kimberlyM24": UserInDB(**{"username":"kimberlyM24",
                            "password":"g2m1e5-M24",
                            "balance":1000000}),

    "ivanH05": UserInDB(**{"username":"ivanH05",
                            "password":"g2m1e5-H05",
                            "balance":1000000}),

    "yamidO15": UserInDB(**{"username":"yamidO15",
                            "password":"g2m1e5-O15",
                            "balance":1000000})                                                                               
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
