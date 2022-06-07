# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Excel.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
                               QVBoxLayout, QWidget)

from Clases.CheckableComboBox import CheckableComboBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1144, 822)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 231, 31))
        font = QFont()
        font.setFamilies([u"Caladea"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.genera_excel = QPushButton(Dialog)
        self.genera_excel.setObjectName(u"genera_excel")
        self.genera_excel.setGeometry(QRect(1030, 790, 101, 25))
        font1 = QFont()
        font1.setFamilies([u"DejaVu Sans"])
        font1.setPointSize(12)
        self.genera_excel.setFont(font1)
        self.atras_excel = QPushButton(Dialog)
        self.atras_excel.setObjectName(u"atras_excel")
        self.atras_excel.setGeometry(QRect(920, 790, 91, 25))
        self.atras_excel.setFont(font1)
        self.qtab = QTabWidget(Dialog)
        self.qtab.setObjectName(u"qtab")
        self.qtab.setGeometry(QRect(10, 80, 1121, 701))
        font2 = QFont()
        font2.setPointSize(11)
        self.qtab.setFont(font2)
        self.qtab.setStyleSheet(u"")
        self.qtab.setMovable(True)
        self.tabla = QWidget()
        self.tabla.setObjectName(u"tabla")
        self.tableWidget = QTableWidget(self.tabla)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 110, 1101, 551))
        self.layoutWidget = QWidget(self.tabla)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 344, 28))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.carga_excel = QPushButton(self.layoutWidget)
        self.carga_excel.setObjectName(u"carga_excel")
        self.carga_excel.setFont(font2)

        self.horizontalLayout.addWidget(self.carga_excel)

        self.pushButton_3 = QPushButton(self.tabla)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 60, 131, 25))
        self.pushButton = QPushButton(self.tabla)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(990, 30, 121, 31))
        self.qtab.addTab(self.tabla, "")
        self.imagen = QWidget()
        self.imagen.setObjectName(u"imagen")
        self.horizontalLayoutWidget = QWidget(self.imagen)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1091, 641))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.verticalSpacer_5 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_11.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_11)

        self.verticalSpacer_6 = QSpacerItem(20, 14, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(21)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.comboBox = CheckableComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(91)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.select_all = QPushButton(self.horizontalLayoutWidget)
        self.select_all.setObjectName(u"select_all")

        self.horizontalLayout_4.addWidget(self.select_all)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.carga_imagen = QPushButton(self.horizontalLayoutWidget)
        self.carga_imagen.setObjectName(u"carga_imagen")

        self.horizontalLayout_2.addWidget(self.carga_imagen)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.verticalLayout.addWidget(self.label_14)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(28)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.carga_imagen_2 = QPushButton(self.horizontalLayoutWidget)
        self.carga_imagen_2.setObjectName(u"carga_imagen_2")

        self.horizontalLayout_3.addWidget(self.carga_imagen_2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(121, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 183, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_12 = QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_12)

        self.label_15 = QLabel(self.horizontalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_15)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.qtab.addTab(self.imagen, "")

        self.retranslateUi(Dialog)

        self.qtab.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"GENERADOR DE ARCHIVOS", None))
        self.genera_excel.setText(QCoreApplication.translate("Dialog", u"Generar", None))
        self.atras_excel.setText(QCoreApplication.translate("Dialog", u"<Atr\u00e1s", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Selecciona la tabla:", None))
        self.carga_excel.setText(QCoreApplication.translate("Dialog", u"Abrir Tabla", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Seleccionar todo", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"MongoDB", None))
        self.qtab.setTabText(self.qtab.indexOf(self.tabla), QCoreApplication.translate("Dialog", u"Tabla", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Configuraci\u00f3n de la imagen", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Selecciona los campos a colocar:", None))
        self.select_all.setText(QCoreApplication.translate("Dialog", u"Seleccionar todo", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Selecciona la imagen:", None))
        self.carga_imagen.setText(QCoreApplication.translate("Dialog", u"Carga imagen", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Configuraci\u00f3n de los par\u00e1metros", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Selecciona las coordenadas:", None))
        self.carga_imagen_2.setText(QCoreApplication.translate("Dialog", u"Conseguir Coordenadas", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Esta es tu imagen seleccionada", None))
        self.label_15.setText("")
        self.qtab.setTabText(self.qtab.indexOf(self.imagen), QCoreApplication.translate("Dialog", u"Imagen", None))
    # retranslateUi
