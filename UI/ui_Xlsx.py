# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'XlsxYnpqbA.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1129, 484)
        self.widget_xlsx = QWidget(Form)
        self.widget_xlsx.setObjectName(u"widget_xlsx")
        self.widget_xlsx.setGeometry(QRect(0, 10, 1121, 471))
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
        font = QFont()
        font.setFamilies([u"MS PGothic"])
        font.setPointSize(20)
        self.ChargeLabel.setFont(font)
        self.ChargeLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ChargeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.ChargeLabel)

        self.btn_charge = QPushButton(self.verticalLayoutWidget_2)
        self.btn_charge.setObjectName(u"btn_charge")
        font1 = QFont()
        font1.setFamilies([u"Leelawadee UI"])
        font1.setPointSize(12)
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ChargeLabel.setText(QCoreApplication.translate("Form", u"Cargar Excel", None))
        self.btn_charge.setText(QCoreApplication.translate("Form", u"Cargar", None))
        self.patients_label.setText(QCoreApplication.translate("Form", u"Pacientes Cargados", None))
        self.patients_result.setText(QCoreApplication.translate("Form", u"-", None))
        self.consulation_label.setText(QCoreApplication.translate("Form", u"Consultas Cargadas", None))
        self.consulation_result.setText(QCoreApplication.translate("Form", u"-", None))
        self.history_label.setText(QCoreApplication.translate("Form", u"Antecedentes Cargados", None))
        self.history_result.setText(QCoreApplication.translate("Form", u"-", None))
    # retranslateUi

