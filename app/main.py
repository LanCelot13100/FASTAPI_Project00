from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field



app = FastAPI()  # <- our App


class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool


@app.post("/create_user")
async def create_user(user: UserCreate):
    return {"name": user.name, "email": user.email, "age": user.age, "is_subscribed": user.is_subscribed}