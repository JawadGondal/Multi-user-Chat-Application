from sqlalchemy import create_engine, column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
import os 
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

