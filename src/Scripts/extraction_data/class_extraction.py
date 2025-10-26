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

    def get_patient_data(self, df: pd.DataFrame) -> list[Patient]:
        validator = Validator()
        patien_list = []
        self.PatientCounter = len(df)
        for index, row in df.iterrows():
            patient = validator.validate_patient_data(row=row)
            if patient:
                patien_list.append(patient)
            else:
                print(f"Fila {index} no válida y será omitida.")
        return patien_list

    def get_consulation_data(self, df: pd.DataFrame) -> list[Consulation]:
        validator = Validator()
        consulation_list = []
        self.ConsulationCounter = len(df)
        for index, row in df.iterrows():
            consulation = validator.validate_consulation_data(row=row)
            if consulation:
                consulation_list.append(consulation)
            else:
                print(f"Fila {index} no válida y será omitida.")
        return consulation_list

    def get_history_data(self, df: pd.DataFrame) -> list[History]:
        validator = Validator()
        history_list = []
        self.HistoryCounter = len(df)
        for index, row in df.iterrows():
            history = validator.validate_history_data(row=row)
            if history:
                history_list.append(history)
            else:
                print(f"Fila {index} no válida y será omitida.")
        return history_list