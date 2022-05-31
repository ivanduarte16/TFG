import os
import tkinter as tk

import cv2
import imutils
import pandas as pd
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QScreen, QAction, QKeySequence, QIcon, QImage
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem

from Bienvenido import Bienvenido
from CheckableComboBox import CheckableComboBox
from Excel import Ui_Dialog
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
    def __init__(self):
        super(Configuracion, self).__init__()

        self.configuracion = Ui_MainWindow()
        self.configuracion.setupUi(self)


class Excel(QMainWindow):

    def __init__(self):
        super(Excel, self).__init__()

        PROJECT_FOLDER = os.path.dirname(os.path.dirname(__file__))  # Quitar si no tienes carpeta de recursos

        self.jpg = None
        self.porcentaje = None
        self.tmp = None
        self.pixmap = None
        self.ventana = None
        self.configuracion = None
        self.items = []
        self.posiciones = []
        self.contador = 0
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

        # Colocamos el icono en el botón
        self.ui_excel.pushButton.setIcon(QIcon('601137-200.png'))

        # Conectamos con la función de escoger el color
        self.ui_excel.pushButton.clicked.connect(self.color_picker)

        # Creamos un combobox donde se introducirán los campos a elegir
        self.comboboxHeaders = CheckableComboBox()

        # Rellenamos el combobox de las fuentes
        self.rellenar_fuentes()

    def center(self):
        """
        Función para centrar la ventana
        """
        centerpoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fg = self.frameGeometry()
        fg.moveCenter(centerpoint)
        self.move(fg.topLeft())

    def rellenar_fuentes(self):
        """
        Función para rellenar el combobox del tamaño de las fuentes
        """
        for x in range(100):
            self.ui_excel.comboBox_fontsize.addItem(str(x))
        self.ui_excel.comboBox_fontsize.setEditable(True)
        self.ui_excel.comboBox_fontsize.setMaxVisibleItems(10)

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
        self.tmp = image
        image = imutils.resize(image, width=381)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.ui_excel.label_15.setPixmap(QtGui.QPixmap.fromImage(image))

    def open_image(self):
        """
        Función para abrir la imagen
        """
        self.contador = 0
        self.posiciones = []
        self.imagen = cv2.imread(self.ui_excel.lineEdit.text(), cv2.IMREAD_UNCHANGED)
        cv2.imshow('image', self.escaled())
        self.configuration()

    def check_image(self):
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
        if event == cv2.EVENT_LBUTTONDOWN and self.contador < len(checked_items):
            ejeX = x
            ejeY = y

            print('Coordenadas: ', ejeX, ',', ejeY)
            strxy = str(ejeX) + ',' + str(ejeY)
            fuente = self.ui_excel.comboBox_font.currentText()
            texto = self.items[checked_items[self.contador]]
            cv2.putText(self.imagen, texto, (int((x * 100) / self.porcentaje), int((y * 100) / self.porcentaje)),
                        self.fuentes[fuente],
                        int(self.ui_excel.comboBox_fontsize.currentText()), self.convertido,
                        2)
            cv2.imshow('image', self.escaled())
            self.contador += 1

    def escaled(self):
        """
        Archivo que guardará la configuracion del escalado para la imagen
        :return: Devolverá los parámetros de la imagen escalada
        """

        # Dimensiones originales
        height = int(self.imagen.shape[0])
        widht = int(self.imagen.shape[1])

        # Dimensiones de mi pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Escalado de mi pantalla
        escalado_width = (65 * screen_width) / 100
        escaldo_height = (65 * screen_height) / 100

        # Porcentaje de las dimensiones de la imagen relativas a mi pantalla
        self.porcentaje = 0

        # Comprobamos que lado es más grande para hacer la regla de tres
        if height > widht:
            self.porcentaje = (escaldo_height * 100) / height
        elif widht > height:
            self.porcentaje = (escalado_width * 100) / widht

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
        self.configuracion = Configuracion()
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

    def color_picker(self):
        """
        Función para escoger el color del texto y convertirlo en formato BGR
        """
        self.color = QtWidgets.QColorDialog.getColor()
        if self.color.isValid():
            self.ui_excel.label_7.setStyleSheet("background-color: {}".format(self.color.name()))
            h = self.color.name().lstrip('#')
            self.convertido = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
            print('Color: ', self.convertido)
            self.convertido = (self.convertido[2], self.convertido[1], self.convertido[0])

    def obtener_info(self):
        for row in range(self.ui_excel.tableWidget.rowCount()):
            if self.ui_excel.tableWidget.item(row, 0).checkState() == Qt.CheckState.Checked:
                print([self.ui_excel.tableWidget.item(row, col).text() for col in
                       range(self.ui_excel.tableWidget.columnCount())])

    def open_excel(self):
        """
        Función que se encargará de buscar archivos excel y rellenar nuestra tabla
        """
        file = QFileDialog.getOpenFileName(self, "Abrir Archivo Excel", "", "Excel Files (*.xlsx) ;; All Files (*)")
        self.direccion = file[0]

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
