# app/utils.py

from sqlalchemy.orm import Session
from . import models

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()
