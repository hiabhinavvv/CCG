from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import declarative_base
from .database import engine  # ✅ Import from database.py

Base = declarative_base()

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

if not all ([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
    raise ValueError("Database credentials are not set in the environment.")

DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True)
    difficulty = Column(String(255), nullable=False)
    date_created = Column(DateTime, default=datetime.now)
    created_by = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    options = Column(String(1024), nullable=False)
    correct_answer_id = Column(Integer, nullable=False)
    explanation = Column(String(2048), nullable=False)


class ChallengeQuota(Base):
    __tablename__ = "challenge_quotas"


    id = Column(Integer, primary_key=True)
    user_id=Column(String(255), nullable=False, unique=True)
    quota_remaining = Column(Integer, nullable=False, default=50)
    last_reset_date = Column(DateTime, default=datetime.now)



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()