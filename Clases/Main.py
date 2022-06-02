from PySide6.QtCore import QSize
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication

from UI.Bienvenido import Bienvenido
from Clases.Generador import Excel


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()

        # Importamos la interfaz de inicio
        self.windowExcel = None
        self.ui_entrada = Bienvenido()
        self.ui_entrada.setupUi(self)

        # Llamamos a la función para centrar la ventana
        self.center()

        # Establecemos un tamaño fijo a la ventana
        self.setFixedSize(QSize(799, 550))

        # Establecemos título a la ventana
        self.setWindowTitle("Generador de Documentos")

        # Llamamos a la función cada vez que el botón sea presionado
        self.ui_entrada.next_button.clicked.connect(self.cambio_ventanas)

        # Llamamos a la función para cerrar la app
        self.ui_entrada.cancel_button.clicked.connect(self.salir)

    def cambio_ventanas(self):
        """
        Función que cambiará a una ventana o a otra en función del radiobutton seleccionado
        """
        self.windowExcel = Excel()
        self.windowExcel.show()
        self.close()

    def salir(self):
        """
        Función para cerrar la aplicación
        """
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirmación")
        dlg.setText("Estas seguro que quieres salir")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button = dlg.exec_()

        if button == QMessageBox.Yes:
            self.close()

    def center(self):
        """
        Función para centrar la ventana
        """
        centerpoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fg = self.frameGeometry()
        fg.moveCenter(centerpoint)
        self.move(fg.topLeft())


app = QApplication([])
window = Main()
window.show()
app.exec()