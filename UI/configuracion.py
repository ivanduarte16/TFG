# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuracion.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QHBoxLayout, QLabel,
                               QPushButton, QSpinBox,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(416, 403)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 100, 161, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 121, 17))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 251, 17))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(True)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 100, 81, 21))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 100, 16, 21))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 100, 16, 21))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 100, 81, 21))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 370, 151, 25))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 300, 391, 61))
        self.label_13.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
                                    "background-color: rgb(246, 245, 244);")
        self.label_13.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 140, 391, 27))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout.addWidget(self.label_7)

        self.comboBox_font = QComboBox(self.layoutWidget)
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.setObjectName(u"comboBox_font")
        font3 = QFont()
        font3.setPointSize(10)
        self.comboBox_font.setFont(font3)

        self.horizontalLayout.addWidget(self.comboBox_font)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 180, 391, 28))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_8.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.spinBox = QSpinBox(self.layoutWidget1)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(500)
        self.spinBox.setSingleStep(1)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(7, 220, 391, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setPointSize(11)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"background-color: rgb(119, 118, 123);")

        self.horizontalLayout_3.addWidget(self.label_10)

        self.pushButton_2 = QPushButton(self.layoutWidget2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777198, 16777215))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"image: url(:/prefijoNuevo/601137-200.png);")
        icon = QIcon()
        iconThemeName = u"color_picker"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/prefijoNuevo/601137-200.png", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 260, 271, 27))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.comboBox_fontsize_2 = QComboBox(self.layoutWidget3)
        self.comboBox_fontsize_2.setObjectName(u"comboBox_fontsize_2")

        self.horizontalLayout_4.addWidget(self.comboBox_fontsize_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Campo elegido:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Configuracion de los campos", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label_6.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Guardar coordendas", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Este es tu texto", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipo de fuente:", None))
        self.comboBox_font.setItemText(0, QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_SIMPLEX", None))
        self.comboBox_font.setItemText(1, QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_PLAIN", None))
        self.comboBox_font.setItemText(2, QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_DUPLEX", None))
        self.comboBox_font.setItemText(3, QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_COMPLEX", None))
        self.comboBox_font.setItemText(4, QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_TRIPLEX", None))
        self.comboBox_font.setItemText(5, QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_COMPLEX_SMALL", None))
        self.comboBox_font.setItemText(6,
                                       QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_SCRIPT_SIMPLEX", None))
        self.comboBox_font.setItemText(7,
                                       QCoreApplication.translate("MainWindow", u"FONT_HERSHEY_SCRIPT_COMPLEX", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o de la fuente:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Color de la fuente:", None))
        self.label_10.setText("")
        self.pushButton_2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Grosor de la letra:", None))
    # retranslateUi
