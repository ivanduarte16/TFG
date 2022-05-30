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
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
                               QTableWidget, QWidget)

from CheckableComboBox import CheckableComboBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1134, 830)
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
        self.tableWidget.setGeometry(QRect(10, 70, 1101, 571))
        self.obtener_info = QPushButton(self.tabla)
        self.obtener_info.setObjectName(u"obtener_info")
        self.obtener_info.setGeometry(QRect(940, 20, 171, 31))
        self.obtener_info.setFont(font2)
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

        self.qtab.addTab(self.tabla, "")
        self.imagen = QWidget()
        self.imagen.setObjectName(u"imagen")
        self.label_3 = QLabel(self.imagen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 200, 221, 21))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.layoutWidget1 = QWidget(self.imagen)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 250, 479, 117))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(58)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777198, 16777215))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"image: url(:/prefijoNuevo/601137-200.png);")
        icon = QIcon()
        iconThemeName = u"color_picker"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/prefijoNuevo/601137-200.png", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_font = QComboBox(self.layoutWidget1)
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.addItem("")
        self.comboBox_font.setObjectName(u"comboBox_font")
        font4 = QFont()
        font4.setPointSize(10)
        self.comboBox_font.setFont(font4)

        self.gridLayout.addWidget(self.comboBox_font, 0, 1, 1, 2)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"background-color: rgb(119, 118, 123);")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.comboBox_fontsize = QComboBox(self.layoutWidget1)
        self.comboBox_fontsize.setObjectName(u"comboBox_fontsize")

        self.gridLayout.addWidget(self.comboBox_fontsize, 1, 1, 1, 2)

        self.layoutWidget2 = QWidget(self.imagen)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 80, 631, 101))
        self.gridLayout_2 = QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.lineEdit = QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.carga_imagen = QPushButton(self.layoutWidget2)
        self.carga_imagen.setObjectName(u"carga_imagen")

        self.horizontalLayout_2.addWidget(self.carga_imagen)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(37)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_10 = QLabel(self.layoutWidget2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.comboBox = CheckableComboBox(self.layoutWidget2)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(91)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.layoutWidget2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.imagen)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(730, 90, 371, 251))
        self.label_11 = QLabel(self.imagen)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 40, 251, 21))
        self.label_11.setFont(font3)
        self.label_12 = QLabel(self.imagen)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(730, 40, 291, 21))
        self.label_12.setFont(font3)
        self.label_13 = QLabel(self.imagen)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 390, 481, 131))
        self.label_13.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
                                    "background-color: rgb(246, 245, 244);")
        self.label_13.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.layoutWidget3 = QWidget(self.imagen)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 600, 511, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setSpacing(28)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.carga_imagen_2 = QPushButton(self.layoutWidget3)
        self.carga_imagen_2.setObjectName(u"carga_imagen_2")

        self.horizontalLayout_3.addWidget(self.carga_imagen_2)

        self.label_14 = QLabel(self.imagen)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 560, 301, 21))
        self.label_14.setFont(font3)
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
        self.obtener_info.setText(QCoreApplication.translate("Dialog", u"Obtener informaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Selecciona la tabla:", None))
        self.carga_excel.setText(QCoreApplication.translate("Dialog", u"Abrir Tabla", None))
        self.qtab.setTabText(self.qtab.indexOf(self.tabla), QCoreApplication.translate("Dialog", u"Tabla", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Configuraci\u00f3n del texto", None))
        self.pushButton.setText("")
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Color de la fuente:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Elije el tipo de fuente:", None))
        self.comboBox_font.setItemText(0, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_SIMPLEX", None))
        self.comboBox_font.setItemText(1, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_PLAIN", None))
        self.comboBox_font.setItemText(2, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_DUPLEX", None))
        self.comboBox_font.setItemText(3, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_COMPLEX", None))
        self.comboBox_font.setItemText(4, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_TRIPLEX", None))
        self.comboBox_font.setItemText(5, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_COMPLEX_SMALL", None))
        self.comboBox_font.setItemText(6, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_SCRIPT_SIMPLEX", None))
        self.comboBox_font.setItemText(7, QCoreApplication.translate("Dialog", u"FONT_HERSHEY_SCRIPT_COMPLEX", None))

        self.label_7.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tama\u00f1o de la fuente:", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Selecciona la imagen:", None))
        self.carga_imagen.setText(QCoreApplication.translate("Dialog", u"Carga imagen", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Selecciona los campos a colocar:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Configuraci\u00f3n de la imagen", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Esta es tu imagen seleccionada", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Este es tu texto", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Selecciona las coordenadas:", None))
        self.carga_imagen_2.setText(QCoreApplication.translate("Dialog", u"Conseguir Coordenadas", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Configuraci\u00f3n de los par\u00e1metros", None))
        self.qtab.setTabText(self.qtab.indexOf(self.imagen), QCoreApplication.translate("Dialog", u"Imagen", None))
    # retranslateUi
