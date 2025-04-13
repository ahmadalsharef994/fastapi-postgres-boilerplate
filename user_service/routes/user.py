# --- user_service/routes/user.py ---

from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy.orm import Session
from ..db import get_db
from ..models.User import User
from ..auth.jwt_handler import create_access_token, decode_token

router = APIRouter(prefix="/user", tags=["User"])


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


@router.post("/register")
def register(email: str, password: str, role: str, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
    user = User(email=email, password=password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully", "user_id": user.id}


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email, "role": user.role, "user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}


def require_role(required_role: str):
    def checker(Authorization: str = Header(...)):
        token = Authorization.split(" ")[1] if " " in Authorization else Authorization
        decoded = decode_token(token)
        if not decoded or decoded.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return decoded
    return checker


@router.get("/me")
def get_profile(user=Depends(require_role("candidate"))):