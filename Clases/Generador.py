import os
import tkinter as tk

import cv2
import imutils
import numpy as np
import pandas as pd
from PIL import ImageFont, ImageDraw, Image
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QScreen, QAction, QKeySequence, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem

from Clases.CheckableComboBox import CheckableComboBox
from Clases.Configuracion import Configuracion
from Clases.Parametros import Parametros
from UI.Excel import Ui_Dialog

root = tk.Tk()


class Excel(QMainWindow):
    def __init__(self):
        super(Excel, self).__init__()

        self.PROJECT_FOLDER = os.path.dirname(os.path.dirname(__file__))
        self.SAVE_FOLDER = os.path.join(self.PROJECT_FOLDER, 'generado')
        self.FONT_PATH = os.path.join(self.PROJECT_FOLDER, 'fonts')

        # Establecemos un tamaño fijo a la ventana
        self.setFixedSize(QSize(1134, 822))

        # Diccionario para guardar los datos de los clics del usuario
        self.parametros: dict[str, Parametros] = {}

        self.seleccionados = None
        self.file = None
        self.current_font_size = None
        self.current_font_name = None
        self.jpg = None
        self.porcentaje = None
        self.tmp = None
        self.pixmap = None
        self.ventana = None
        self.items = []
        self.cabeceras = None
        self.convertido = None
        self.color = None
        self.imagen = None
        self.columnas = None
        self.welcome = None
        self.direccion = None

        self.configuracion = Configuracion(self)
        self.ui_excel = Ui_Dialog()
        self.ui_excel.setupUi(self)

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

        # Creamos un combobox donde se introducirán los campos a elegir
        self.comboboxHeaders = CheckableComboBox()

        # Conectamos con la función para seleccionar todos los campos de la tabla
        self.ui_excel.pushButton_3.clicked.connect(self.select_all_checkboxes)

        # Conectamos con la función de generar los documentos
        self.ui_excel.genera_excel.clicked.connect(self.generator)

        # Conectamos con la función para seleccionar/des seleccionar todos los campos del combobox
        self.ui_excel.select_all.clicked.connect(self.ui_excel.comboBox.change_checked_items)

        self.ui_excel.horizontalLayout_5.setEnabled(False)

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
            ejeX = (x * 100) / self.porcentaje
            ejeY = (y * 100) / self.porcentaje

            # Colocamos las coordenadas en los line edits
            self.configuracion.configuracion.label_3.setText(str(int(ejeX)))
            self.configuracion.configuracion.label_6.setText(str(int(ejeY)))

            # Variable donde guardaremos el texto que está dentro del combobox dentro de la ui de configuracion
            texto = self.configuracion.configuracion.comboBox.currentText()

            # Variable donde guardaremos el grosor de la fuente que está dentro del combobox dentro de la ui de configuracion
            grosor = self.configuracion.configuracion.comboBox_fontsize_2.currentText()

            # Guardamos en el diccionario en la key "texto" un objeto Parametros que contiene toda la info del clic
            self.parametros[texto] = Parametros(texto, (int(ejeX), int(ejeY)), self.current_font_name,
                                                int(self.current_font_size), self.convertido, int(grosor))

            # Cargamos de nuevo la imagen para que esté limpia
            self.imagen = cv2.imread(self.ui_excel.lineEdit.text(), cv2.IMREAD_UNCHANGED)

            # Añadimos los campos que el usuario ya ha establecido
            self.add_texts()

            # Finalmente mostramos la imagen con todas las modificaciones
            cv2.imshow('image', self.escaled())

    def add_texts(self, valor=None):
        """
        Función para añadir los textos que el usuario ya ha establecido
        """
        # Obtenemos las Key del diccionario
        for key in self.parametros.keys():

            # Obtenemos el objeto Parametros de la key que hemos obtenido anteriormente y lo guardamos en una variable
            parametro = self.parametros[key]

            for ruta in os.listdir(self.FONT_PATH):
                if parametro.tipo_fuente in ruta:
                    fuente = os.path.join(self.FONT_PATH, ruta)

            font = ImageFont.truetype(fuente, parametro.tam_fuente)
            img_pil = Image.fromarray(self.imagen)
            draw = ImageDraw.Draw(img_pil)
            color = list(parametro.color)
            color.append(0)
            color = tuple(color)
            draw.text(parametro.coordenadas, parametro.nombre if valor is None else valor[self.items.index(key)],
                      font=font, fill=color)
            self.imagen = np.array(img_pil)

    def escaled(self):
        """
        Archivo que guardará la configuracion del escalado para la imagen
        :return: Devolverá los parámetros de la imagen escalada
        """

        # Dimensiones originales de la imagen
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

        # Si cerramos la ventana se cerrará la ventana de confi
        wait_time = 1000
        while cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) >= 1:
            keyCode = cv2.waitKey(wait_time)
            if (keyCode & 0xFF) == ord("q"):
                self.configuracion.close()
                cv2.destroyAllWindows()
                break
        cv2.waitKey(0)

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

        # Comprobamos que el archivo seleccionados es el correcto
        except ValueError:
            QMessageBox.about(self, 'Información', 'Formato incorrecto')
            return None

        # Comprobamos que se ha seleccionados un archivo
        except FileNotFoundError:
            QMessageBox.about(self, 'Información', 'No se ha seleccionados ningún archivo')
            return None

        self.ui_excel.tableWidget.setRowCount(y)
        self.ui_excel.tableWidget.setColumnCount(x)
        self.columnas = self.ui_excel.tableWidget.columnCount()
        self.ui_excel.comboBox.clear()

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
        self.ui_excel.horizontalLayout_5.setEnabled(True)

    def generator(self):
        """
        Función que generará los documentos y los guardará
        """
        print("Estos son los datos que vamos a tratar: ", '\n')
        self.seleccionados = []
        for row in range(self.ui_excel.tableWidget.rowCount()):
            if self.ui_excel.tableWidget.item(row, 0).checkState() == Qt.CheckState.Checked:
                self.seleccionados.append([self.ui_excel.tableWidget.item(row, col).text() for col in
                                           range(self.ui_excel.tableWidget.columnCount())])
        for i in self.seleccionados:
            self.imagen = cv2.imread(self.ui_excel.lineEdit.text(), cv2.IMREAD_UNCHANGED)
            self.add_texts(valor=i)
            print("Generando documento para: " + i[1])
            save_name = i[1] + "_" + i[0].replace(" ", "_") + ".jpg"
            save_name = os.path.join(self.SAVE_FOLDER, save_name)
            cv2.imwrite(save_name, self.imagen)
