# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUivezNzw.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1127, 613)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 470, 291, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderLabel = QLabel(self.verticalLayoutWidget)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(20)
        self.HeaderLabel.setFont(font)
        self.HeaderLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.HeaderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.HeaderLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_excel = QPushButton(self.verticalLayoutWidget)
        self.btn_excel.setObjectName(u"btn_excel")
        font1 = QFont()
        font1.setFamilies([u"Leelawadee UI"])
        font1.setPointSize(12)
        self.btn_excel.setFont(font1)
        self.btn_excel.setStyleSheet(u"QPushButton {\n"
"    background-color: #24d467;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #24d467;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_excel)

        self.btn_json = QPushButton(self.verticalLayoutWidget)
        self.btn_json.setObjectName(u"btn_json")
        self.btn_json.setFont(font1)
        self.btn_json.setStyleSheet(u"QPushButton {\n"
"    background-color: #F54927;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #F54927;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_json)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.widget_xlsx = QWidget(self.centralwidget)
        self.widget_xlsx.setObjectName(u"widget_xlsx")
        self.widget_xlsx.setGeometry(QRect(-10, 0, 1121, 461))
        self.charge_box = QWidget(self.widget_xlsx)
        self.charge_box.setObjectName(u"charge_box")
        self.charge_box.setGeometry(QRect(920, 390, 201, 71))
        self.verticalLayoutWidget_2 = QWidget(self.charge_box)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 201, 65))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ChargeLabel = QLabel(self.verticalLayoutWidget_2)
        self.ChargeLabel.setObjectName(u"ChargeLabel")
        self.ChargeLabel.setFont(font)
        self.ChargeLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ChargeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.ChargeLabel)

        self.btn_charge = QPushButton(self.verticalLayoutWidget_2)
        self.btn_charge.setObjectName(u"btn_charge")
        self.btn_charge.setFont(font1)
        self.btn_charge.setStyleSheet(u"QPushButton {\n"
"    background-color: #24d467;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #24d467;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_charge)

        self.widget_result_xlsx = QWidget(self.widget_xlsx)
        self.widget_result_xlsx.setObjectName(u"widget_result_xlsx")
        self.widget_result_xlsx.setGeometry(QRect(10, 0, 911, 451))
        self.horizontalLayoutWidget_2 = QWidget(self.widget_result_xlsx)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 70, 911, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.patients_label = QLabel(self.horizontalLayoutWidget_2)
        self.patients_label.setObjectName(u"patients_label")
        self.patients_label.setFont(font)
        self.patients_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.patients_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.patients_label)

        self.patients_result = QLabel(self.horizontalLayoutWidget_2)
        self.patients_result.setObjectName(u"patients_result")
        self.patients_result.setFont(font)
        self.patients_result.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.patients_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.patients_result)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.consulation_label = QLabel(self.horizontalLayoutWidget_2)
        self.consulation_label.setObjectName(u"consulation_label")
        self.consulation_label.setFont(font)
        self.consulation_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.consulation_label)

        self.consulation_result = QLabel(self.horizontalLayoutWidget_2)
        self.consulation_result.setObjectName(u"consulation_result")
        self.consulation_result.setFont(font)
        self.consulation_result.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.consulation_result)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.history_label = QLabel(self.horizontalLayoutWidget_2)
        self.history_label.setObjectName(u"history_label")
        self.history_label.setFont(font)
        self.history_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.history_label)

        self.history_result = QLabel(self.horizontalLayoutWidget_2)
        self.history_result.setObjectName(u"history_result")
        self.history_result.setFont(font)
        self.history_result.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.history_result)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(900, 520, 211, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_json_3 = QPushButton(self.horizontalLayoutWidget)
        self.btn_json_3.setObjectName(u"btn_json_3")
        self.btn_json_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_json_3)

        self.btn_json_2 = QPushButton(self.horizontalLayoutWidget)
        self.btn_json_2.setObjectName(u"btn_json_2")
        self.btn_json_2.setFont(font1)
        self.btn_json_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #e3171a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #e3171a;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_json_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1127, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Tipo de Archivo", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"XLSX", None))
        self.btn_json.setText(QCoreApplication.translate("MainWindow", u"JSON", None))
        self.ChargeLabel.setText(QCoreApplication.translate("MainWindow", u"Cargar Excel", None))
        self.btn_charge.setText(QCoreApplication.translate("MainWindow", u"Cargar", None))
        self.patients_label.setText(QCoreApplication.translate("MainWindow", u"Pacientes Cargados", None))
        self.patients_result.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.consulation_label.setText(QCoreApplication.translate("MainWindow", u"Consultas Cargadas", None))
        self.consulation_result.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.history_label.setText(QCoreApplication.translate("MainWindow", u"Antecedentes Cargados", None))
        self.history_result.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_json_3.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.btn_json_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

