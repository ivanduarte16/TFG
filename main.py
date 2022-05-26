import os

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLabel, \
    QPushButton, QLineEdit, QStackedLayout, QDialogButtonBox, QDialog, QMessageBox


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.reject = None
        self.setWindowTitle("Calculadora")

        # Creamos el menu con un separador
        menu = self.menuBar()
        file_menu = menu.addMenu("&Menu")
        file_menu.addSeparator()

        # Creamos un submenu para los modos de normal y cientifica
        file_submenu = file_menu.addMenu("Modos")
        file_menu.addSeparator()

        # Creamos el boton de guardar
        self.guardar = QAction("&Guardar", self)
        self.guardar.setShortcut(QKeySequence("Ctrl+s"))
        self.guardar.triggered.connect(self.guardarArchivo)
        file_menu.addAction(self.guardar)
        file_menu.addSeparator()

        # Creamos el boton se salir
        salir = QAction("&Salir", self)
        salir.setShortcut(QKeySequence("Ctrl+q"))
        salir.triggered.connect(self.salirVentana)
        file_menu.addAction(salir)

        # Añadimos el boton que mostrara la calculadora normal
        self.button_normal = QAction("Normal", self)
        self.statusBar().showMessage("Estas en el modo normal")

        # Conectamos con la funcion para mostrarla
        self.button_normal.triggered.connect(self.cambiaNormal)

        # Añadimos el boton al submenu
        file_submenu.addAction(self.button_normal)

        # Añadimos el boton que mostrara la calculadora cientifica
        button_cientifica = QAction("Cientifica", self)

        # Conectamos con la funcion para mostrarla
        button_cientifica.triggered.connect(self.cambiCientifico)

        # Añadimos el boton al submenu
        file_submenu.addAction(button_cientifica)

        # Creamos los grgid layput que contendran los botones de las calculadoras
        self.grid_normal = QGridLayout()
        self.grid_normal.setSpacing(10)
        self.grid_cientifico = QGridLayout()
        self.grid_cientifico.setSpacing(10)

        # Creamos los widgets que contendran los grid layouts y los añadimos
        # Widget caculadora normal
        self.widget_normal = QWidget()
        self.widget_normal.setLayout(self.grid_normal)
        # Widget cientifico
        self.widget_cientifico = QWidget()
        self.widget_cientifico.setLayout(self.grid_cientifico)

        # Stacklayout que contendra los dos widgets e ira alternando y se los añadimos
        self.stack = QStackedLayout()
        self.stack.addWidget(self.widget_normal)
        self.stack.addWidget(self.widget_cientifico)

        # Creamos el widget que contendra el stack y se lo añadimos
        self.widget_stack = QWidget()
        self.widget_stack.setLayout(self.stack)

        # Definimos un line edit donde se mostraran los numeros
        # Tambien le estableceremos un tamaño y tamaño de fuente alineados a la derecha
        self.pantalla = QLineEdit()
        self.pantalla.setFixedHeight(60)
        fuente = self.pantalla.font()
        fuente.setPointSize(30)
        self.pantalla.setFont(fuente)
        self.pantalla.setAlignment(Qt.AlignRight)

        # Creamos el layout que contendrá el line edit y el widget del stack y le añadimos estos dos
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pantalla)
        self.layout.addWidget(self.widget_stack)

        # Creamos el widget principal
        self.widget_principal = QWidget()

        # Añadimos al widget principal el layout
        self.widget_principal.setLayout(self.layout)
        self.setCentralWidget(self.widget_principal)

        # Establecemos los botones de la calculadora normal
        self.normal = ['raiz', 'pi', '^', '!',
                       'AC', '(', ')', "/",
                       '7', '8', '9', '*',
                       '4', '5', '6', '+',
                       '1', '2', '3', '-',
                       "0", ".", "<-", "="]

        # Asignamos las posiciones a los botones de la calculadora normal
        self.posisiones = [(i, j) for i in range(6) for j in range(4)]

        # Recoremos la lista de botones y por cada boton la asociaremos la posicion
        for self.posisiones, self.normal in zip(self.posisiones, self.normal):
            # Creamos el boton
            boton = QPushButton(self.normal)
            # Conectamos el boton con la funcion operacion
            boton.clicked.connect(self.operacion)
            # Añadimos al gridLatout cada boton
            self.grid_normal.addWidget(boton, *self.posisiones)

        # Establecemos los botones de la calculadora cientifica
        self.cientifica = ['Rad', 'Deg', 'x!', '(', ')', '%', 'AC',
                           'Inv', 'sin', 'In', "7", '8', '9', '/',
                           'π', 'cos', 'log', '4', '5', '6', '*',
                           'e', 'tan', '√', '1', '2', '3', '-',
                           'Ans', 'EXP', '^', '0', '.', '=', '+']

        # Asignamos las posiciones a los botones de la calculadora cientifica
        self.posisiones2 = [(i, j) for i in range(5) for j in range(7)]

        # Recoremos la lista de botones y por cada boton la asociaremos la posicion
        for self.posisiones2, self.cientifica in zip(self.posisiones2, self.cientifica):
            # Creamos el boton
            boton = QPushButton(self.cientifica)
            # Conectamos el boton con la funcion operacion
            boton.clicked.connect(self.operacion)
            # Añadimos al gridLatout cada boton
            self.grid_cientifico.addWidget(boton, *self.posisiones2)

        # Establecemos una cadena vacia
        self.cadena = ""

    def operacion(self):
        """
        Funcion que dependiendo del string que contenga cada boton se comportara de una forma o otra
        """

        # Comprobaremos la tecla de borrar y le borraremos un caracter de la cadena
        if self.sender().text() == "<-":
            self.editarTexto(self.cadena[:-1])
            self.cadena = self.cadena[:-1]

        # Comprobaremos la tecla de igual y llamara a la funcion resultado
        elif self.sender().text() == "=":
            self.calcular_resultado()

        # Borraremos lo que hay en pantalla
        elif self.sender().text() == "AC":
            self.editarTexto("")
            self.cadena = ""

        else:
            self.cadena += self.sender().text()
            self.editarTexto(self.cadena)

    def editarTexto(self, texto):
        """
        Esta funcion se encargará de mostrar por pantalla los numeros, operadores ...
        :param texto: String que recibira para modificar
        """
        self.pantalla.setText(texto)
        self.pantalla.setFocus()

    def calcular_resultado(self):
        """
        Funcion que calculara el resultado de la operacion introducida
        """
        self.editarTexto(str(eval(self.cadena)))

    def cambiaNormal(self):
        """
        Esta funcion cambiara a modo normal la calculadora
        """
        self.statusBar().showMessage("Estas en el modo normal")
        self.pantalla.setText("")
        self.stack.setCurrentIndex(0)

    def cambiCientifico(self):
        """
        Esta funcion cambiara a modo cientifico la calculadora
        """
        self.statusBar().showMessage("Estas en el modo cientifico")
        self.pantalla.setText("")
        self.stack.setCurrentIndex(1)

    def guardarArchivo(self):
        """
        Funcion para guardar los datos en el fichero de texto
        """
        fichero = os.path.join(os.path.dirname(__file__), "historial.txt")
        with open(fichero, "a") as f:
            f.write(self.pantalla.text() + "\n")
            f.close()

    def salirVentana(self):
        """
        Funcion para cerrar la aplicacion
        """
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Confirmacion")
        dlg.setText("Estas seguro que quieres salir")
        dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        button = dlg.exec_()

        if button == QMessageBox.Yes:
            self.close()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
