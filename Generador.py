import os
import tkinter as tk

import cv2
import imutils
import pandas as pd
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QScreen, QAction, QKeySequence, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem

from Bienvenido import Bienvenido
from CheckableComboBox import CheckableComboBox
from Excel import Ui_Dialog
from Parametros import Parametros
from configuracion import Ui_MainWindow

root = tk.Tk()


class Welcome(QMainWindow):

    def __init__(self):
        super(Welcome, self).__init__()

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


class Configuracion(QMainWindow):
    def __init__(self, mainwindow):
        super(Configuracion, self).__init__()

        self.setWindowTitle("Configuracion")

        # Importamos la clase principal del programa para poder acceder a sus variables y modificarlas
        self.main_window: Excel = mainwindow

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


class Excel(QMainWindow):

    def __init__(self):
        super(Excel, self).__init__()

        PROJECT_FOLDER = os.path.dirname(os.path.dirname(__file__))

        self.file = None
        self.current_font_size = None
        self.current_font_name = None
        self.jpg = None
        self.porcentaje = None
        self.tmp = None
        self.pixmap = None
        self.ventana = None
        self.configuracion = Configuracion(self)
        self.items = []

        # Diccionario para guardar los datos de los clicks del usuario
        self.parametros: dict[str, Parametros] = {}

        self.posiciones = []
        self.cabeceras = None
        self.convertido = None
        self.color = None
        self.imagen = None
        self.columnas = None
        self.welcome = None
        self.direccion = None

        self.ui_excel = Ui_Dialog()
        self.ui_excel.setupUi(self)

        # Creamos un diccionario para que acceda con la llave del combobox
        self.fuentes = {
            "FONT_HERSHEY_SIMPLEX": cv2.FONT_HERSHEY_SIMPLEX,
            "FONT_HERSHEY_PLAIN": cv2.FONT_HERSHEY_PLAIN,
            "FONT_HERSHEY_DUPLEX": cv2.FONT_HERSHEY_DUPLEX,
            "FONT_HERSHEY_COMPLEX": cv2.FONT_HERSHEY_COMPLEX,
            "FONT_HERSHEY_TRIPLEX": cv2.FONT_HERSHEY_TRIPLEX,
            "FONT_HERSHEY_COMPLEX_SMALL": cv2.FONT_HERSHEY_COMPLEX_SMALL,
            "FONT_HERSHEY_SCRIPT_SIMPLEX": cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
            "FONT_HERSHEY_SCRIPT_COMPLEX": cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        }

        # Centramos la ventana
        self.center()

        # Cambia a la anterior ventana
        self.ui_excel.atras_excel.clicked.connect(self.change_back)

        # Desactivar edición de ruta
        self.ui_excel.lineEdit.setReadOnly(True)

        # Al elegir una imagen, comprueba si tiene texto o no para activar/desactivar el botón
        self.ui_excel.lineEdit.textChanged.connect(self.check_image)

        # Creamos el menu con un separador
        menu = self.menuBar()
        file_menu = menu.addMenu("&Menu")
        file_menu.addSeparator()

        # Creamos un submenu para los modos de normal y científica
        file_submenu = file_menu.addMenu("Modos")
        file_menu.addSeparator()

        # Creamos el botón de salir
        salir = QAction("&Salir", self)
        salir.setShortcut(QKeySequence("Ctrl+q"))
        salir.triggered.connect(self.exit)
        file_menu.addAction(salir)

        # Llamamos a la función para abrir nuestra tabla excel
        self.ui_excel.carga_excel.clicked.connect(self.open_excel)

        # Llamamos a la función para cargar la ruta de la imagen
        self.ui_excel.carga_imagen.clicked.connect(self.image_path)

        # Abre la imagen en una ventana
        self.ui_excel.carga_imagen_2.clicked.connect(self.open_image)

        # Conectamos con la función para obtener los campos en una lista
        self.ui_excel.obtener_info.clicked.connect(self.obtener_info)

        # Creamos un combobox donde se introducirán los campos a elegir
        self.comboboxHeaders = CheckableComboBox()

        # Conectamos con la función para seleccionar todos los campos de la tabla
        self.ui_excel.pushButton_3.clicked.connect(self.select_all_checkboxes)

    def center(self):
        """
        Función para centrar la ventana
        """
        centerpoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fg = self.frameGeometry()
        fg.moveCenter(centerpoint)
        self.move(fg.topLeft())

    def change_back(self):
        """
        Función para cambiar de ventana a la anterior
        """
        self.welcome = Welcome()
        self.welcome.show()
        self.close()

    def exit(self):
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

    def image_path(self):
        """
        Función para buscar en el explorador de archivos los archivos tipo png, jpg...
        """
        img = QFileDialog.getOpenFileName(self, "Abrir Imágenes", "", "Image Files (*.png *.jpg *jpeg)")
        self.ui_excel.lineEdit.setText(str(img[0]))
        self.jpg = cv2.imread(img[0])
        self.setPhoto(self.jpg)

    def setPhoto(self, image):
        """
        Función para mostrar la imagen en la ventana
        :param image: Imagen a mostrar
        """
        self.tmp = image
        image = imutils.resize(image, width=381)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.ui_excel.label_15.setPixmap(QtGui.QPixmap.fromImage(image))

    def open_image(self):
        """
        Función para abrir la imagen
        """
        self.posiciones = []
        names = []
        for pos in self.ui_excel.comboBox.get_checked_items():
            names.append(self.items[pos])
        self.configuracion.configuracion.comboBox.clear()
        self.configuracion.configuracion.comboBox.addItems(names)
        self.imagen = cv2.imread(self.ui_excel.lineEdit.text(), cv2.IMREAD_UNCHANGED)
        cv2.imshow('image', self.escaled())
        self.configuration()

    def check_image(self):
        """
        Función que comprará si hay texto en el line edit para ponerlo en no editable
        """
        if self.ui_excel.lineEdit.text() == "":
            self.ui_excel.carga_imagen_2.setDisabled(True)
        else:
            self.ui_excel.carga_imagen_2.setEnabled(True)

    def click_event(self, event, x, y, flags, param):
        """
        Función para saber las coordenadas en pixeles de la imagen para colocar el texto
        :param event:
        :param x:
        :param y:
        :param flags:
        :param param:
        """
        checked_items = self.ui_excel.comboBox.get_checked_items()
        if event == cv2.EVENT_LBUTTONDOWN:
            ejeX = x
            ejeY = y

            print('Coordenadas: ', ejeX, ',', ejeY)

            # Colocamos las coordenadas en los line edits
            self.configuracion.configuracion.label_3.setText(str(ejeX))
            self.configuracion.configuracion.label_6.setText(str(ejeY))

            # Variable donde guardaremos el texto que está dentro del combobox dentro de la ui de configuracion
            texto = self.configuracion.configuracion.comboBox.currentText()

            # Guardamos en el diccionario en la key "texto" un objeto Parametros que contiene toda la info del clic
            self.parametros[texto] = Parametros(texto, (int(ejeX), int(ejeY)), self.fuentes[self.current_font_name], int(self.current_font_size), self.convertido)

            # Cargamos de nuevo la imagen para que esté limpia
            self.imagen = cv2.imread(self.ui_excel.lineEdit.text(), cv2.IMREAD_UNCHANGED)

            # Añadimos los campos que el usuario ya ha establecido
            self.add_texts()

            # Finalmente mostramos la imagen con todas las modificaciones
            cv2.imshow('image', self.escaled())

    def add_texts(self):
        """
        Función para añadir los textos que el usuario ya ha establecido
        """
        print(self.parametros)
        # Obtenemos las Key del diccionario
        for key in self.parametros.keys():
            # Obtenemos el objeto Parametros de la key que hemos obtenido anteriormente y lo guardamos en una variable
            parametro = self.parametros[key]
            # Colocamos el texto en la imagen
            cv2.putText(self.imagen, parametro.nombre, (int((parametro.coordenadas[0] * 100) / self.porcentaje), int((parametro.coordenadas[1] * 100) / self.porcentaje)),
                        parametro.tipo_fuente,
                        parametro.tam_fuente, parametro.color,
                        2)

    def escaled(self):
        """
        Archivo que guardará la configuracion del escalado para la imagen
        :return: Devolverá los parámetros de la imagen escalada
        """

        # Dimensiones originales
        height = int(self.imagen.shape[0])
        width = int(self.imagen.shape[1])

        # Dimensiones de mi pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Escalado de mi pantalla
        escalado_width = (65 * screen_width) / 100
        escaldo_height = (65 * screen_height) / 100

        # Porcentaje de las dimensiones de la imagen relativas a mi pantalla
        self.porcentaje = 0

        # Comprobamos que lado es más grande para hacer la regla de tres
        if height > width:
            self.porcentaje = (escaldo_height * 100) / height
        elif width > height:
            self.porcentaje = (escalado_width * 100) / width

        # Calculamos la altura y el ancho de la imagen aplicándole el porcentaje
        altura = int(self.imagen.shape[0] * self.porcentaje / 100)
        ancho = int(self.imagen.shape[1] * self.porcentaje / 100)
        tamaño = (ancho, altura)

        return cv2.resize(self.imagen, tamaño, interpolation=cv2.INTER_AREA)

    def configuration(self):
        """
        En esta función se mostrará la imagen con el tamaño ya escalado
        """
        cv2.imshow("image", self.escaled())
        self.configuracion.show()
        cv2.setMouseCallback("image", self.click_event)

        wait_time = 1000
        # Si cerramos la ventana se cerrará la ventana de confi
        while cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) >= 1:
            keyCode = cv2.waitKey(wait_time)
            if (keyCode & 0xFF) == ord("q"):
                self.configuracion.close()
                cv2.destroyAllWindows()
                break
        cv2.waitKey(0)

    def obtener_info(self):
        """
        En esta función se obtendrá
        """
        for row in range(self.ui_excel.tableWidget.rowCount()):
            if self.ui_excel.tableWidget.item(row, 0).checkState() == Qt.CheckState.Checked:
                print([self.ui_excel.tableWidget.item(row, col).text() for col in
                       range(self.ui_excel.tableWidget.columnCount())])

    def select_all_checkboxes(self):
        """
        Función para seleccionar o deseleccionar todos los campos de la tabla
        """
        if self.ui_excel.tableWidget.rowCount() > 0:
            if self.ui_excel.tableWidget.item(0, 0).checkState() == Qt.CheckState.Checked:
                for row in range(self.ui_excel.tableWidget.rowCount()):
                    self.ui_excel.tableWidget.item(row, 0).setCheckState(Qt.CheckState.Unchecked)
            else:
                for row in range(self.ui_excel.tableWidget.rowCount()):
                    self.ui_excel.tableWidget.item(row, 0).setCheckState(Qt.CheckState.Checked)

    def open_excel(self):
        """
        Función que se encargará de buscar archivos excel y rellenar nuestra tabla
        """
        self.file = QFileDialog.getOpenFileName(self, "Abrir Archivo Excel", "",
                                                "Excel Files (*.xlsx) ;; All Files (*)")
        self.direccion = self.file[0]

        try:
            df = pd.read_excel(self.direccion)
            columnas = list(df.columns)
            df_fila = df.to_numpy().tolist()
            x = len(columnas)
            y = len(df_fila)

        # Comprobamos que el archivo seleccionado es el correcto
        except ValueError:
            QMessageBox.about(self, 'Información', 'Formato incorrecto')
            return None

        # Comprobamos que se ha seleccionado un archivo
        except FileNotFoundError:
            QMessageBox.about(self, 'Información', 'No se ha seleccionado ningún archivo')
            return None

        # print(x, y)
        self.ui_excel.tableWidget.setRowCount(y)
        self.ui_excel.tableWidget.setColumnCount(x)
        self.columnas = self.ui_excel.tableWidget.columnCount()

        # Rellenamos las celdas con los datos del excel
        for col in range(x):
            self.cabeceras = QtWidgets.QTableWidgetItem(columnas[col])
            self.ui_excel.tableWidget.setColumnWidth(col, 250)
            self.ui_excel.tableWidget.setHorizontalHeaderItem(col, self.cabeceras)

            # Añadimos las cabeceras de las columnas al combobox con un checkbox
            self.ui_excel.comboBox.addItem(columnas[col])
            self.ui_excel.comboBox.setItemChecked(col, False)
            self.items.append(columnas[col])

            # Comprobamos que si el campo está vacío dejarlo como está
            for row in range(y):
                item = str(df_fila[row][col])
                if item == 'nan':
                    item = ''
                self.ui_excel.tableWidget.setItem(row, col, QTableWidgetItem(item))

                # Colocamos los checkboxes en las celdas de la primera columna
                if col % self.columnas == 0:
                    objecto = QTableWidgetItem(item)
                    objecto.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    objecto.setCheckState(Qt.CheckState.Unchecked)
                    self.ui_excel.tableWidget.setItem(row, col, objecto)


app = QApplication([])
window = Welcome()
window.show()
app.exec()
