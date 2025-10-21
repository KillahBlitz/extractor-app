from pydantic import BaseModel
from datetime import datetime

class Consulation(BaseModel):
    id_patient: int
    date: datetime
    weight: float
    height: float
    observations: str 
    medications: str = ""   