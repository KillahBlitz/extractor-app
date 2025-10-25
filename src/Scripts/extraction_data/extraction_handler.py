import pandas as pd
from PySide6.QtWidgets import QFileDialog


def upload_xlsx_file():
    file_path, _ = QFileDialog.getOpenFileName(None,"Seleccionar archivo Excel","","Archivos Excel (*.xlsx *.xls);;Todos los archivos (*)")
    if not file_path:
        return None
    try:
        #buscar la hoja llamada "pacientes"
        df_patients = pd.read_excel(file_path, sheet_name="pacientes")
        #buscar la hoja llamada "consultas"
        df_consulation = pd.read_excel(file_path, sheet_name="consultas")
        #buscar la hoja llamada "antecedentes"
        df_history = pd.read_excel(file_path, sheet_name="antecedentes")
        if df_patients is None or df_consulation is None or df_history is None:
            return None
        return df_patients, df_consulation, df_history
    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return None
    
def upload_json_file():
    file_path, _ = QFileDialog.getOpenFileName(None,"Seleccionar archivo JSON","","Archivos JSON (*.json);;Todos los archivos (*)")
    if not file_path:
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        return data
    except Exception as e:
        print("Error al leer el archivo JSON:", e)
        return None