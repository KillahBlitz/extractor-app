import sys
# Configurar rutas del proyecto
from config.config import setup_project_paths
setup_project_paths()

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from UI.ui_MainUi import Ui_MainWindow
from UI.ui_Xlsx import Ui_Form as Ui_Form_Xlsx
from UI.ui_Json import Ui_Form as Ui_Form_Json
from src.Scripts.extraction_data.extraction_handler import upload_xlsx_file, upload_json_file


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Extractor App")
        
        # Crear widgets para xlsx y json
        self.xlsx_widget = QWidget()
        self.json_widget = QWidget()
        
        # Configurar la interfaz xlsx
        self.xlsx_ui = Ui_Form_Xlsx()
        self.xlsx_ui.setupUi(self.xlsx_widget)
        self.xlsx_widget.setParent(self.ui.widget_data)
        self.xlsx_widget.resize(self.ui.widget_data.size())
        self.xlsx_widget.hide()

        # Configurar la interfaz json
        self.json_ui = Ui_Form_Json()
        self.json_ui.setupUi(self.json_widget)
        self.json_widget.setParent(self.ui.widget_data)
        self.json_widget.resize(self.ui.widget_data.size())
        self.json_widget.hide()
        
        #buttons connections
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_excel.clicked.connect(lambda: self.show_data("xlsx"))
        self.ui.btn_json.clicked.connect(lambda: self.show_data("json"))

    def show_data(self, type_data):
        self.ui.widget_data.show()
        if type_data == "xlsx":
            self.json_widget.hide()
            self.xlsx_widget.show()
            if hasattr(self.xlsx_ui, 'widget_result_xlsx'):
                self.xlsx_ui.widget_result_xlsx.hide()
            if hasattr(self.xlsx_ui, 'btn_upload_xlsx'):
                self.xlsx_ui.btn_upload_xlsx.clicked.connect(self.show_xlsx_results)
                
        if type_data == "json":
            self.xlsx_widget.hide()
            self.json_widget.show()
            if hasattr(self.json_ui, 'widget_result_json'):
                self.json_ui.widget_result_json.hide()
            if hasattr(self.json_ui, 'btn_upload_json'):
                self.json_ui.btn_upload_json.clicked.connect(self.show_json_results)
    
    def show_xlsx_results(self):
        result = upload_xlsx_file()
        if result and isinstance(result, dict) and result.get('success'):
            if hasattr(self.xlsx_ui, 'widget_result_xlsx'):
                self.xlsx_ui.widget_result_xlsx.show()
            counters = result.get('counters', {})
            
            # Datos cargados desde Excel
            self.xlsx_ui.patients_load.setText(str(counters.get('patients_loaded', 0)))
            self.xlsx_ui.consulation_load.setText(str(counters.get('consulations_loaded', 0)))
            self.xlsx_ui.history_load.setText(str(counters.get('histories_loaded', 0)))
            
            # Datos validados
            self.xlsx_ui.patients_valid.setText(str(counters.get('patients_valid', 0)))
            self.xlsx_ui.consulation_valid.setText(str(counters.get('consulations_valid', 0)))
            self.xlsx_ui.history_valid.setText(str(counters.get('histories_valid', 0)))
            
            # Datos guardados (por ahora iguales a los validados)
            self.xlsx_ui.patients_result.setText(str(counters.get('patients_injected', 0)))
            self.xlsx_ui.consulation_result.setText(str(counters.get('consulations_injected', 0)))
            self.xlsx_ui.history_result.setText(str(counters.get('histories_injected', 0)))
            
        else:
            self.error_message("Error al cargar el archivo Excel.")
    
    def show_json_results(self):
        status = upload_json_file()
        if hasattr(self.json_ui, 'widget_result_json') and status:
            self.json_ui.widget_result_json.show()
        else:
            self.error_message("Error al cargar el archivo JSON.")

    def error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())