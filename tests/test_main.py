# test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_health_check():
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_patient():
    # Assuming you have an endpoint for creating a patient
    patient_data = {"name": "John Doe", "age": 30, "gender": "Male"}
    response = client.post("/patients", json=patient_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


def test_get_patient():
    # Assuming you have an endpoint for getting patient details
    response = client.get("/patients/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
