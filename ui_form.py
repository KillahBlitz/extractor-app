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
from PySide6.QtWidgets import (QApplication, QPushButton, QRadioButton, QSizePolicy,
    QToolButton, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.toolButton = QToolButton(Widget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(250, 240, 23, 23))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 180, 80, 24))
        self.radioButton = QRadioButton(Widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(320, 350, 91, 22))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.toolButton.setText(QCoreApplication.translate("Widget", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", u"RadioButton", None))
    # retranslateUi

