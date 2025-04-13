# --- user_service/routes/user.py ---
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
from user_service.db import get_db
from user_service.models import User


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(email: str, password: str, role: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=email, password=password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
