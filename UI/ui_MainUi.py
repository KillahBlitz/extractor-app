# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUiKAjkPB.ui'
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
        MainWindow.resize(1120, 623)
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

        self.widget_data = QWidget(self.centralwidget)
        self.widget_data.setObjectName(u"widget_data")
        self.widget_data.setGeometry(QRect(-10, 0, 1121, 461))
        self.charge_box = QWidget(self.widget_data)
        self.charge_box.setObjectName(u"charge_box")
        self.charge_box.setGeometry(QRect(920, 390, 201, 71))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(900, 520, 211, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_reload = QPushButton(self.horizontalLayoutWidget)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setFont(font1)

        self.horizontalLayout_2.addWidget(self.btn_reload)

        self.btn_exit = QPushButton(self.horizontalLayoutWidget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setFont(font1)
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"    background-color: #e3171a;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white;\n"
"    color: #e3171a;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_exit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1120, 33))
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
        self.btn_reload.setText(QCoreApplication.translate("MainWindow", u"Reload", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

