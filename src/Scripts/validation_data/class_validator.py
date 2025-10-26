from models.class_patient import Patient
from models.class_history import History
from models.class_consulation import Consulation

from datetime import datetime, date

class Validator:
    patient_valid_count = 0
    consulation_valid_count = 0 
    history_valid_count = 0

    def validate_patient_data(self, row):
        try:
            name = str(row['Nombre del paciente'])
            age = int(row['Edad'])
            type_patient = str(row['Tipo de paciente'])
            weight = float(row['Peso'])
            height = float(row['Altura'])
            total_consultations = float(row['Numero totales de registros'])
            patient = Patient(
                name=name,
                age=age,
                type_patient=type_patient,
                weight=weight,
                height=height,
                total_consultations=total_consultations
            )
            self.patient_valid_count += 1
            return patient
        except Exception as e:
            print("Error de validación de paciente:", e)
            return False
        
    def validate_consulation_data(self, row):
        try:
            name = str(row['Nombre del paciente'])
            weight = float(row['Peso'])
            height = float(row['Altura'])
            observations = str(row['Observaciones'])
            medications = str(row['Medicamentos'])
            
            fecha_raw = row['Fecha']
            if hasattr(fecha_raw, 'date'): 
                consult_date = fecha_raw.date()
            else:
                consult_date = fecha_raw.date()

            consulation = Consulation(
                name=name,
                date=consult_date,
                weight=weight,
                height=height,
                observations=observations,
                medications=medications
            )
            self.consulation_valid_count += 1
            return consulation
        
        except Exception as e:
            print("Error de validación de consulta:", e)
            return False
    
    def validate_history_data(self, row):
        try:
            name = str(row['Nombre del paciente'])
            history = str(row['Antecedente'])
            type_history = str(row['Tipo de antecedente'])
            history = History(
                name=name,
                history=history,
                type_history=type_history
            )
            self.history_valid_count += 1
            return history
        except Exception as e:
            print("Error de validación de historia:", e)
            return False