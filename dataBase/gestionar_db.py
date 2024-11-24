import sqlite3

# Conexión a la base de datos
def conectar():
    return sqlite3.connect("empacuenta.db")

# Agregar un ingrediente
def agregar_ingrediente(nombre, precio_por_unidad, unidad_medida):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
        INSERT INTO Ingredientes (nombre, precio_por_unidad, unidad_medida)
        VALUES (?, ?, ?)
        """, (nombre, precio_por_unidad, unidad_medida))
        conexion.commit()
        print(f"Ingrediente '{nombre}' agregado con éxito.")
    except sqlite3.Error as e:
        print(f"Error al agregar ingrediente: {e}")
    finally:
        conexion.close()

# Agregar una receta
def agregar_receta(nombre_empanada, ingredientes):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        # Crear la receta
        cursor.execute("""
        INSERT INTO Recetas (nombre_empanada)
        VALUES (?)
        """, (nombre_empanada,))
        id_receta = cursor.lastrowid

        # Relacionar los ingredientes con la receta
        for ingrediente_id, cantidad in ingredientes:
            cursor.execute("""
            INSERT INTO Recetas_Ingredientes (id_receta, id_ingrediente, cantidad)
            VALUES (?, ?, ?)
            """, (id_receta, ingrediente_id, cantidad))

        conexion.commit()
        print(f"Receta '{nombre_empanada}' creada con éxito.")
    except sqlite3.Error as e:
        print(f"Error al agregar receta: {e}")
    finally:
        conexion.close()
