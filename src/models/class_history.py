from pydantic import BaseModel

class history(BaseModel):
    id_patient: int
    history: str
    type_history: str = "N/A"