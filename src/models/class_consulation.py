from pydantic import BaseModel
from datetime import date

class Consulation(BaseModel):
    name: str
    date: date
    weight: float
    height: float
    pc: float
    observations: str