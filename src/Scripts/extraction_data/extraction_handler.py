from Scripts.extraction_data.class_extraction import Extractor
from Scripts.injection_data.injector_handler import inject_data_to_db

from PySide6.QtWidgets import QFileDialog
import pandas as pd

def upload_xlsx_file():
    file_path, _ = QFileDialog.getOpenFileName(None,"Seleccionar archivo Excel","","Archivos Excel (*.xlsx *.xls);")
    if not file_path:
        return None
    try:
        extractor = Extractor()
        df_patients = pd.read_excel(file_path, sheet_name="pacientes")
        df_consulation = pd.read_excel(file_path, sheet_name="consultas")
        df_history = pd.read_excel(file_path, sheet_name="antecedentes")
        if df_patients is None or df_consulation is None or df_history is None:
            return None
        
        patients = extractor.get_patient_data(df_patients)
        consulations = extractor.get_consulation_data(df_consulation)
        histories = extractor.get_history_data(df_history)
        
        pi, ci, hi = inject_data_to_db(patients, consulations, histories)
        
        return {
            'success': True,
            'counters': {
                'patients_loaded': extractor.PatientCounter,
                'consulations_loaded': extractor.ConsulationCounter,
                'histories_loaded': extractor.HistoryCounter,
                'patients_valid': len(patients),
                'consulations_valid': len(consulations),
                'histories_valid': len(histories),
                'patients_injected': pi,
                'consulations_injected': ci,
                'histories_injected': hi
            }
        }

    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return None
    
def upload_json_file():
    file_path, _ = QFileDialog.getOpenFileName(None,"Seleccionar archivo JSON","","Archivos JSON (*.json);")
    if not file_path:
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        return data
    except Exception as e:
        print("Error al leer el archivo JSON:", e)
        return None