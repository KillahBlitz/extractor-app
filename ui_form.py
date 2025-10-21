# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1231, 600)
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(390, 160, 451, 251))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 221, 20))
        font = QFont()
        font.setFamilies([u"Berlin Sans FB"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.btn_readexcel = QPushButton(self.frame)
        self.btn_readexcel.setObjectName(u"btn_readexcel")
        self.btn_readexcel.setGeometry(QRect(110, 100, 80, 24))
        font1 = QFont()
        font1.setBold(True)
        self.btn_readexcel.setFont(font1)
        self.btn_readjson = QPushButton(self.frame)
        self.btn_readjson.setObjectName(u"btn_readjson")
        self.btn_readjson.setGeometry(QRect(260, 100, 80, 24))
        self.btn_readjson.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u00bfEn que forrmato esta el archivo?", None))
        self.btn_readexcel.setText(QCoreApplication.translate("Widget", u"EXCEL", None))
        self.btn_readjson.setText(QCoreApplication.translate("Widget", u"JSON", None))
    # retranslateUi

