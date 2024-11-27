import sqlite3
def inicializar_base_datos():
    conexion = sqlite3.connect("empacuenta.db")
    cursor = conexion.cursor()

    # Crear tablas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingredientes (
        id_ingrediente INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio_por_unidad REAL NOT NULL,
        unidad_medida TEXT NOT NULL CHECK (unidad_medida IN ('kg', 'litro', 'unidad', 'otro'))
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recetas (
        id_receta INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_empanada TEXT NOT NULL,
        costo_total REAL DEFAULT 0
    );
    """)

    # Agrega el resto de las tablas aquí

# Crear tabla Recetas_Ingredientes (relación)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recetas_Ingredientes (
        id_receta INTEGER,
        id_ingrediente INTEGER,
        cantidad REAL NOT NULL,
        PRIMARY KEY (id_receta, id_ingrediente),
        FOREIGN KEY (id_receta) REFERENCES Recetas(id_receta),
        FOREIGN KEY (id_ingrediente) REFERENCES Ingredientes(id_ingrediente)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produccion (
        id_produccion INTEGER PRIMARY KEY AUTOINCREMENT,
        id_receta INTEGER,
        cantidad_producida INTEGER NOT NULL,
        fecha DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (id_receta) REFERENCES Recetas(id_receta)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ventas (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_receta INTEGER,
        cantidad_vendida INTEGER NOT NULL,
        fecha DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (id_receta) REFERENCES Recetas(id_receta)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inversiones (
        id_inversion INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        costo REAL NOT NULL,
        fecha_adquisicion DATE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS GastosFijos (
        id_gasto_fijo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
        monto REAL NOT NULL,
        frecuencia TEXT NOT NULL CHECK (frecuencia IN ('mensual', 'anual'))
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DeudasProveedores (
        id_deuda INTEGER PRIMARY KEY AUTOINCREMENT,
        proveedor TEXT NOT NULL,
        monto REAL NOT NULL,
        fecha_vencimiento DATE NOT NULL,
        estado TEXT NOT NULL CHECK (estado IN ('pendiente', 'pagado'))
    );
    """)

    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    inicializar_base_datos()