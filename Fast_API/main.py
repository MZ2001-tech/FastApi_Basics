from fastapi import FastAPI
from uuid import UUID, uuid4
from typing import List
from .models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Zikry",
        last_name="Shukry",
        gender=Gender.male,
        roles=[Role.student, Role.admin]
    ),
    User(
        id=uuid4(), 
        first_name="Ayna",
        last_name="Saffiyah",
        gender=Gender.female,
        roles=[Role.student, Role.user]
    ),
]

@app.get("/")
async def root():
    return {"Hello": "Zikry"} 

@app.get("/api/v1/users")
async def fetch_users():
    return db
