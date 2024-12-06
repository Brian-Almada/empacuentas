import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from dataBase.gestionar_db import agregar_ingrediente
from dataBase.consultas_db import listar_ingredientes

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar la interfaz desde el archivo .ui
        loadUi("gui/main_window.ui", self)


        # Conectar botones con las funciones correspondientes
        self.btnAgregarIngrediente.clicked.connect(self.agregar_ingrediente)
        self.btnListarIngredientes.clicked.connect(self.listar_ingredientes)

    def agregar_ingrediente(self):
        """Agrega un nuevo ingrediente a la base de datos."""
        # Obtén los datos de los campos de entrada
        nombre = self.lineNombreIngrediente.text()
        try:
            precio = float(self.linePrecioIngrediente.text())
        except ValueError:
            print("Error: El precio debe ser un número válido.")
            return
        unidad = self.comboUnidadMedida.currentText()

        # Llama a la función para agregar el ingrediente
        agregar_ingrediente(nombre, precio, unidad)

        # Limpia los campos de entrada
        self.lineNombreIngrediente.clear()
        self.linePrecioIngrediente.clear()
        print(f"Ingrediente '{nombre}' agregado correctamente.")

    def listar_ingredientes(self):
        """Muestra los ingredientes en la tabla."""
        # Limpia la tabla antes de llenarla
        self.tableIngredientes.setRowCount(0)

        # Obtén los ingredientes desde la base de datos
        ingredientes = listar_ingredientes()

        # Llena la tabla con los datos obtenidos
        for fila, ingrediente in enumerate(ingredientes):
            self.tableIngredientes.insertRow(fila)
            for columna, dato in enumerate(ingrediente):
                self.tableIngredientes.setItem(fila, columna, QTableWidgetItem(str(dato)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
