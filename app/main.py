from fastapi import FastAPI
from app.routes import app as fastapi_app
from patient import Patient

def main():
    patient1 = Patient(name="John Doe", age=30, weight_kg=75, height_m=1.75)
    patient1.display_info()

if __name__ == "__main__":
    main()
