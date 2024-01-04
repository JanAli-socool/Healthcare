# app/__init__.py

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"  # Use your actual database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
