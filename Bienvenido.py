
from PySide6 import QtCore, QtGui, QtWidgets


class Bienvenido(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 550)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wallpaper = QtWidgets.QLabel(self.centralwidget)
        self.wallpaper.setGeometry(QtCore.QRect(-10, -50, 311, 651))
        self.wallpaper.setStyleSheet("image: url(:/prefijoNuevo/280889_original_4320x7680.jpg);")
        self.wallpaper.setText("")
        self.wallpaper.setPixmap(QtGui.QPixmap(":/cubo/280889_original_4320x7680.jpg"))
        self.wallpaper.setScaledContents(False)
        self.wallpaper.setObjectName("wallpaper")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 20, 411, 51))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 70, 181, 51))
        self.label_5.setObjectName("label_5")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(530, 510, 121, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(670, 510, 101, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 240, 391, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(340, 280, 192, 78))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(13)
        self.splitter.setFont(font)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.sencillo_radio = QtWidgets.QRadioButton(self.splitter)
        self.sencillo_radio.setObjectName("sencillo_radio")
        self.avanzado_radio = QtWidgets.QRadioButton(self.splitter)
        self.avanzado_radio.setObjectName("avanzado_radio")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Bienvenido a tu Generador de"))
        self.label_5.setText(_translate("MainWindow", "Documentos"))
        self.next_button.setText(_translate("MainWindow", "Siguiente >"))
        self.cancel_button.setText(_translate("MainWindow", "Cancelar"))
        self.label_4.setText(_translate("MainWindow", "Selecciona unas de las siguientes opciones:"))
        self.sencillo_radio.setText(_translate("MainWindow", "Sencillo"))
        self.avanzado_radio.setText(_translate("MainWindow", "Avanzado"))
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Bienvenido()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())