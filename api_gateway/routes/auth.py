from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from ..auth.jwt_handler import create_access_token

router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: UserLogin):
    if data.username == "admin" and data.password == "secret":
        return {"access_token": create_access_token({"sub": data.username})}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
