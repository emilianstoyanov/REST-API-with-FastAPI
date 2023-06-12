from fastapi import APIRouter
from models.user import User 
from config.db import conn 
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter()

@user.get("/")
async def find_all_users():
    return serializeList(conn.local.user.find())

@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        password = user.password
    ))
    return conn.execute(users.select()).fetchall()
    

@user.put("/{id}")
async def update_data(id:int, user: User):
    conn.execute(users.update().values(
        name = user.name,
        email = user.email,
        password = user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))