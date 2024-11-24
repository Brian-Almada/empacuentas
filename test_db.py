from dataBase.gestionar_db import agregar_ingrediente, agregar_receta
import sqlite3


# Agregar algunos ingredientes
agregar_ingrediente("Harina", 1.5, "kg")
agregar_ingrediente("Carne", 8.0, "kg")
agregar_ingrediente("Cebolla", 0.5, "kg")
agregar_ingrediente("Aceite", 2.0, "litro")
agregar_ingrediente("Sal", 0.1, "kg")

# Agregar una receta con ingredientes
# Lista de tuplas: (id_ingrediente, cantidad)
try:
    conexion = sqlite3.connect("empacuenta.db")
    cursor = conexion.cursor()

    ingredientes_receta = [
        (1, 1, 0.2),  # id_receta, id_ingrediente, cantidad
        (1, 2, 0.1),
        (1, 3, 0.05),
        (1, 4, 0.01),
        (1, 5, 0.005)
    ]

    for id_receta, id_ingrediente, cantidad in ingredientes_receta:
        # Comprobar si el registro ya existe
        cursor.execute("""
        SELECT COUNT(*) FROM Recetas_Ingredientes
        WHERE id_receta = ? AND id_ingrediente = ?;
        """, (id_receta, id_ingrediente))
        existe = cursor.fetchone()[0]

        if existe == 0:
            cursor.execute("""
            INSERT INTO Recetas_Ingredientes (id_receta, id_ingrediente, cantidad)
            VALUES (?, ?, ?);
            """, (id_receta, id_ingrediente, cantidad))
            print(f"Ingresado: id_receta={id_receta}, id_ingrediente={id_ingrediente}, cantidad={cantidad}")
        else:
            print(f"Ya existe: id_receta={id_receta}, id_ingrediente={id_ingrediente}")

    conexion.commit()
    print("Ingredientes de la receta agregados con éxito.")
except sqlite3.Error as e:
    print(f"Error al agregar ingredientes a la receta: {e}")
finally:
    conexion.close()

