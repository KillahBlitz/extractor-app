import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from UI.ui_MainUi import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Extractor App")
        self.ui.widget_xlsx.hide()
        #buttons
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_excel.clicked.connect(self.show_xlsx)
    
    def show_xlsx(self):
        self.ui.widget_xlsx.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
