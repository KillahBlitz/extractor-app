from pydantic import BaseModel
from datetime import date

class Consulation(BaseModel):
    name: str
    date: date
    weight: float
    height: float
    observations: str 
    medications: str = ""   