# app/routes.py

from fastapi import Depends, HTTPException, status
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from . import crud, models
from .database import SessionLocal, engine

router = APIRouter()

# Your API routes will be defined here using FastAPI's decorators
# Example:
@router.get("/patients/{patient_id}", response_model=models.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
