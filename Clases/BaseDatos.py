from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from PySide6.QtWidgets import QMainWindow, QApplication

from Clases.MongoDB import Mongo, transformar
from UI.MongoDB import Ui_MainWindow


class BaseDatos(QMainWindow):
    def __init__(self, generador):
        super(BaseDatos, self).__init__()

        self.setWindowTitle("Base de Datos")

        # Importamos la clase generador del programa para poder acceder a sus variables y modificarlas
        self.main_window = generador

        self.db: Mongo = Mongo()

        self.base_datos = Ui_MainWindow()
        self.base_datos.setupUi(self)

        self.base_datos.lineEdit.textChanged.connect(self.desactivar_btn_guardar)
        self.desactivar_btn_guardar()

        self.base_datos.comboBox.currentTextChanged.connect(self.desactivar_btn_cargar)
        self.desactivar_btn_cargar()

        self.base_datos.pushButton.clicked.connect(self.cargar_coleccion)
        self.base_datos.pushButton_2.clicked.connect(self.guardar_coleccion)

        self.center()

    def center(self):
        """
        Función para centrar la ventana
        """
        centerpoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        fg = self.frameGeometry()
        fg.moveCenter(centerpoint)
        self.move(fg.topLeft())

    def desactivar_btn_guardar(self):
        if self.main_window.ui_excel.tableWidget.rowCount() == 0 or len(self.base_datos.lineEdit.text()) < 1:
            self.base_datos.pushButton_2.setEnabled(False)
        else:
            self.base_datos.pushButton_2.setEnabled(True)

    # Función para desactivar el botón de cargar si no hay nada seleccionado en el combobox
    def desactivar_btn_cargar(self):
        if self.base_datos.comboBox.currentText() == "":
            self.base_datos.pushButton.setEnabled(False)
        else:
            self.base_datos.pushButton.setEnabled(True)

    def cargar_coleccion(self):
        nombre = self.base_datos.comboBox.currentText()
        col = self.db.get_all(nombre)
        # Cargar los datos en la tabla

    def guardar_coleccion(self):
        nombre = self.base_datos.lineEdit.text()
        datos = []
        # Obtener los datos de la tabla
        seleccionados = []
        for row in range(self.main_window.ui_excel.tableWidget.rowCount()):
            if self.main_window.ui_excel.tableWidget.item(row, 0).checkState() == Qt.CheckState.Checked:
                seleccionados.append([self.main_window.ui_excel.tableWidget.item(row, col).text() for col in
                                      range(self.main_window.ui_excel.tableWidget.columnCount())])

        for selec in seleccionados:
            datos.append(transformar(self.main_window.items, selec))

        self.db.add_multiple(nombre, datos)

        self.close()
