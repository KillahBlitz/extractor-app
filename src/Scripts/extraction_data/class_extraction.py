from models.class_patient import Patient
from models.class_history import History
from models.class_consulation import Consulation
from Scripts.validation_data.class_validator import Validator
from pydantic import BaseModel
import pandas as pd

class Extractor(BaseModel):
    PatientCounter: int = 0
    ConsulationCounter: int = 0
    HistoryCounter: int = 0

    @staticmethod
    def get_patient_data(df: pd.DataFrame) -> list[Patient]:
        validator = Validator()
        patien_list = []
        for index, row in df.iterrows():
            patient = validator.validate_patient_data(row=row)
            if patient:
                patien_list.append(patient)
            else:
                print(f"Fila {index} no válida y será omitida.")
        return patien_list

    @staticmethod
    def get_consulation_data(df: pd.DataFrame) -> list[Consulation]:
        print(df.head())
        return []
        
    @staticmethod
    def get_history_data(df: pd.DataFrame) -> list[History]:
        print(df.head())
        return []