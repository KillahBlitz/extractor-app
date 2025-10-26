from pydantic import BaseModel

class History(BaseModel):
    name: str
    history: str
    type_history: str = "N/A"