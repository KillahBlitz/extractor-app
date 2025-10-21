from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int = 0
    type_patient: str = "N/A"
    weight: float
    height: float
    total_consulation: int = 0