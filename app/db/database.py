# --- app/db/database.py ---
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.Base import Base

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@db:5432/smarthub")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
