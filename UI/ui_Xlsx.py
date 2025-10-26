# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'XlsxdOWVqa.ui'
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
        Form.resize(1129, 497)
        self.widget_xlsx = QWidget(Form)
        self.widget_xlsx.setObjectName(u"widget_xlsx")
        self.widget_xlsx.setGeometry(QRect(0, 0, 1121, 481))
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

        self.btn_upload_xlsx = QPushButton(self.verticalLayoutWidget_2)
        self.btn_upload_xlsx.setObjectName(u"btn_upload_xlsx")
        font1 = QFont()
        font1.setFamilies([u"Leelawadee UI"])
        font1.setPointSize(12)
        self.btn_upload_xlsx.setFont(font1)
        self.btn_upload_xlsx.setStyleSheet(u"QPushButton {\n"
"    background-color: #24d467;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #24d467;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_upload_xlsx)

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

        self.patients_load = QLabel(self.horizontalLayoutWidget_2)
        self.patients_load.setObjectName(u"patients_load")
        self.patients_load.setFont(font)
        self.patients_load.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.patients_load.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.patients_load)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.consulation_label = QLabel(self.horizontalLayoutWidget_2)
        self.consulation_label.setObjectName(u"consulation_label")
        self.consulation_label.setFont(font)
        self.consulation_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.consulation_label)

        self.consulation_load = QLabel(self.horizontalLayoutWidget_2)
        self.consulation_load.setObjectName(u"consulation_load")
        self.consulation_load.setFont(font)
        self.consulation_load.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_load.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.consulation_load)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.history_label = QLabel(self.horizontalLayoutWidget_2)
        self.history_label.setObjectName(u"history_label")
        self.history_label.setFont(font)
        self.history_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.history_label)

        self.history_load = QLabel(self.horizontalLayoutWidget_2)
        self.history_load.setObjectName(u"history_load")
        self.history_load.setFont(font)
        self.history_load.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_load.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.history_load)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalLayoutWidget_4 = QWidget(self.widget_result_xlsx)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 160, 911, 80))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.patients_label_3 = QLabel(self.horizontalLayoutWidget_4)
        self.patients_label_3.setObjectName(u"patients_label_3")
        self.patients_label_3.setFont(font)
        self.patients_label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.patients_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.patients_label_3)

        self.patients_valid = QLabel(self.horizontalLayoutWidget_4)
        self.patients_valid.setObjectName(u"patients_valid")
        self.patients_valid.setFont(font)
        self.patients_valid.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.patients_valid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.patients_valid)


        self.horizontalLayout_6.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.consulation_label_3 = QLabel(self.horizontalLayoutWidget_4)
        self.consulation_label_3.setObjectName(u"consulation_label_3")
        self.consulation_label_3.setFont(font)
        self.consulation_label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.consulation_label_3)

        self.consulation_valid = QLabel(self.horizontalLayoutWidget_4)
        self.consulation_valid.setObjectName(u"consulation_valid")
        self.consulation_valid.setFont(font)
        self.consulation_valid.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_valid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.consulation_valid)


        self.horizontalLayout_6.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.history_label_3 = QLabel(self.horizontalLayoutWidget_4)
        self.history_label_3.setObjectName(u"history_label_3")
        self.history_label_3.setFont(font)
        self.history_label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.history_label_3)

        self.history_valid = QLabel(self.horizontalLayoutWidget_4)
        self.history_valid.setObjectName(u"history_valid")
        self.history_valid.setFont(font)
        self.history_valid.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_valid.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.history_valid)


        self.horizontalLayout_6.addLayout(self.verticalLayout_13)

        self.horizontalLayoutWidget_5 = QWidget(self.widget_result_xlsx)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 250, 911, 80))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.patients_label_4 = QLabel(self.horizontalLayoutWidget_5)
        self.patients_label_4.setObjectName(u"patients_label_4")
        self.patients_label_4.setFont(font)
        self.patients_label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.patients_label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.patients_label_4)

        self.patients_result = QLabel(self.horizontalLayoutWidget_5)
        self.patients_result.setObjectName(u"patients_result")
        self.patients_result.setFont(font)
        self.patients_result.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.patients_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.patients_result)


        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.consulation_label_4 = QLabel(self.horizontalLayoutWidget_5)
        self.consulation_label_4.setObjectName(u"consulation_label_4")
        self.consulation_label_4.setFont(font)
        self.consulation_label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.consulation_label_4)

        self.consulation_result = QLabel(self.horizontalLayoutWidget_5)
        self.consulation_result.setObjectName(u"consulation_result")
        self.consulation_result.setFont(font)
        self.consulation_result.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.consulation_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.consulation_result)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.history_label_4 = QLabel(self.horizontalLayoutWidget_5)
        self.history_label_4.setObjectName(u"history_label_4")
        self.history_label_4.setFont(font)
        self.history_label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.history_label_4)

        self.history_result = QLabel(self.horizontalLayoutWidget_5)
        self.history_result.setObjectName(u"history_result")
        self.history_result.setFont(font)
        self.history_result.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.history_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.history_result)


        self.horizontalLayout_7.addLayout(self.verticalLayout_16)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ChargeLabel.setText(QCoreApplication.translate("Form", u"Cargar Excel", None))
        self.btn_upload_xlsx.setText(QCoreApplication.translate("Form", u"Cargar", None))
        self.patients_label.setText(QCoreApplication.translate("Form", u"Pacientes Cargados", None))
        self.patients_load.setText(QCoreApplication.translate("Form", u"-", None))
        self.consulation_label.setText(QCoreApplication.translate("Form", u"Consultas Cargadas", None))
        self.consulation_load.setText(QCoreApplication.translate("Form", u"-", None))
        self.history_label.setText(QCoreApplication.translate("Form", u"Antecedentes Cargados", None))
        self.history_load.setText(QCoreApplication.translate("Form", u"-", None))
        self.patients_label_3.setText(QCoreApplication.translate("Form", u"Pacientes Validados", None))
        self.patients_valid.setText(QCoreApplication.translate("Form", u"-", None))
        self.consulation_label_3.setText(QCoreApplication.translate("Form", u"Consultas Validadas", None))
        self.consulation_valid.setText(QCoreApplication.translate("Form", u"-", None))
        self.history_label_3.setText(QCoreApplication.translate("Form", u"Antecedentes Validados", None))
        self.history_valid.setText(QCoreApplication.translate("Form", u"-", None))
        self.patients_label_4.setText(QCoreApplication.translate("Form", u"Pacientes Guardados", None))
        self.patients_result.setText(QCoreApplication.translate("Form", u"-", None))
        self.consulation_label_4.setText(QCoreApplication.translate("Form", u"Consultas Guardados", None))
        self.consulation_result.setText(QCoreApplication.translate("Form", u"-", None))
        self.history_label_4.setText(QCoreApplication.translate("Form", u"Antecedentes Guardados", None))
        self.history_result.setText(QCoreApplication.translate("Form", u"-", None))
    # retranslateUi

