from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from UI.configuracion import Ui_MainWindow


class Configuracion(QMainWindow):
    def __init__(self, mainwindow):
        super(Configuracion, self).__init__()

        self.setWindowTitle("Configuracion")

        # Importamos la clase principal del programa para poder acceder a sus variables y modificarlas
        self.main_window = mainwindow

        self.configuracion = Ui_MainWindow()
        self.configuracion.setupUi(self)

        self.convertido = None
        self.color = None

        # Selector de color
        self.configuracion.pushButton_2.clicked.connect(self.color_picker)

        # Al cambiar el valor del comboBox, actualiza el valor de la variable en la clase principal
        self.configuracion.comboBox_fontsize.currentTextChanged.connect(self.change_current_font_size)

        # Al cambiar el valor del comboBox, actualiza el valor de la variable en la clase principal
        self.configuracion.comboBox_font.currentTextChanged.connect(self.change_current_font_name)

        # Cambia la fuente actual a la fuente seleccionada, ya que las funciones de antes solo se llaman cuando el usuario actualiza el combobox
        self.change_current_font_name(self.configuracion.comboBox_font.currentText())

        # Rellenamos el combobox de las fuentes
        self.rellenar_fuentes()

    def color_picker(self):
        """
        Función para escoger el color del texto y convertirlo en formato BGR
        """
        self.color = QtWidgets.QColorDialog.getColor()
        if self.color.isValid():
            self.configuracion.label_10.setStyleSheet("background-color: {}".format(self.color.name()))
            h = self.color.name().lstrip('#')
            self.convertido = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            print('Color: ', self.convertido)
            self.convertido = (self.convertido[2], self.convertido[1], self.convertido[0])
            self.main_window.convertido = self.convertido

    def rellenar_fuentes(self):
        """
        Función para rellenar el combobox del tamaño de las fuentes
        """
        for x in range(100):
            self.configuracion.comboBox_fontsize.addItem(str(x))
        self.configuracion.comboBox_fontsize.setEditable(True)
        self.configuracion.comboBox_fontsize.setMaxVisibleItems(10)

    def change_current_font_name(self, font_name):
        """
        Función para cambiar el nombre de la fuente en el programa principal para luego poder usarla en las funciones
        :param font_name: Nombre de la fuente
        """
        self.main_window.current_font_name = font_name

    def change_current_font_size(self, text):
        """
        Función para cambiar el tamaño de la fuente en el programa principal para luego poder usarla en las funciones
        :param text: Tamaño de la fuente
        """
        self.main_window.current_font_size = text
