from pydantic import BaseModel

class History(BaseModel):
    id_patient: int
    history: str
    type_history: str = "N/A"