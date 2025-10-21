# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #al presionar el boton oculta frame y todo su contenido
        self.ui.btn_readexcel.clicked.connect(self.init_process('excel'))
        self.ui.btn_readjson.clicked.connect(self.init_process('json'))

    def init_process(self, file_type):
        #oculta el frame
        def process():
            self.ui.frame.hide()
            if file_type == 'excel':
                print("Iniciando proceso para archivo EXCEL")
            elif file_type == 'json':
                print("Iniciando proceso para archivo JSON")
                
        return process
    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
