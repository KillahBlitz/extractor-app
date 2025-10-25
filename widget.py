import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from UI.ui_MainUi import Ui_MainWindow
from UI.ui_Xlsx import Ui_Form as Ui_Form_Xlsx
from UI.ui_Json import Ui_Form as Ui_Form_Json


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
        elif type_data == "json":
            self.xlsx_widget.hide()
            self.json_widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
