from models.class_patient import Patient
from models.class_history import History
from models.class_consulation import Consulation
from pydantic import BaseModel
import pandas as pd

class Extractor(BaseModel):
    PatientCounter: int = 0
    ConsulationCounter: int = 0
    HistoryCounter: int = 0

    @staticmethod
    def get_patient_data(df: pd.DataFrame) -> list[Patient]:
        print(df.head())
        return []

    @staticmethod
    def get_consulation_data(df: pd.DataFrame) -> list[Consulation]:
        print(df.head())
        return []
        
    @staticmethod
    def get_history_data(df: pd.DataFrame) -> list[History]:
        print(df.head())
        return []