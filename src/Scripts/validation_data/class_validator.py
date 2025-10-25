from models.class_patient import Patient
from models.class_history import History
from models.class_consulation import Consulation

class Validator:
    #valida si las clases de un modelo cumplen con ciertos criterios
    patient_valid_count = 0
    consulation_valid_count = 0 
    history_valid_count = 0

    #este metodo recibe un row del data frame de pacientes y valida sus datos de acuerdo al modelo de Patient
    def validate_patient_data(self, row) -> bool:
        #guarda en variables los datos del row
        try:
            name = str(row['Nombre del paciente'])
            age = int(row['Edad'])
            type_patient = str(row['Tipo de paciente'])
            weight = float(row['Peso'])
            height = float(row['Altura'])
            total_consultations = float(row['Numero totales de registros'])
            #inicializa la clase de pydantic Patient, si no cumple con el modelo, lanza una excepcion
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