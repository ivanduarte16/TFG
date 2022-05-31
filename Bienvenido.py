# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Bienvenido.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import imagen_fondo

class Bienvenido(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(782, 550)
        font = QFont()
        font.setFamilies([u"DejaVu Sans"])
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.wallpaper = QLabel(self.centralwidget)
        self.wallpaper.setObjectName(u"wallpaper")
        self.wallpaper.setGeometry(QRect(-10, -50, 311, 651))
        self.wallpaper.setStyleSheet(u"image: url(:/imagen_bienvenido/280889_original_4320x7680.jpg);")
        self.wallpaper.setPixmap(QPixmap(u":/cubo/280889_original_4320x7680.jpg"))
        self.wallpaper.setScaledContents(False)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 20, 411, 51))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 70, 181, 51))
        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(530, 510, 121, 25))
        font1 = QFont()
        font1.setFamilies([u"DejaVu Sans"])
        font1.setPointSize(13)
        self.next_button.setFont(font1)
        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(670, 510, 101, 25))
        self.cancel_button.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 240, 401, 16))
        font2 = QFont()
        font2.setFamilies([u"DejaVu Sans"])
        font2.setPointSize(12)
        self.label_4.setFont(font2)
        self.label_4.setInputMethodHints(Qt.ImhNone)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 270, 421, 16))
        self.label_6.setFont(font2)
        self.label_6.setInputMethodHints(Qt.ImhNone)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 300, 421, 16))
        self.label_7.setFont(font2)
        self.label_7.setInputMethodHints(Qt.ImhNone)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.wallpaper.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bienvenido a tu Generador de", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Documentos", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Siguiente >", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dexcel es una app con la que podr\u00e1s generar tus ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"documentos con mucha facilidad, de forma r\u00e1pida", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"y de forma seguridad", None))
    # retranslateUi

