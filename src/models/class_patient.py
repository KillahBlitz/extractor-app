from pydantic import BaseModel
from datetime import date

class Patient(BaseModel):
    name: str
    age: int = 0
    type_patient: str = "N/A"
    weight: float
    height: float
    total_consulation: int = 0
    birthdate: date
    apgar: str