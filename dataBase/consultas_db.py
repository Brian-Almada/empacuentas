import sqlite3

def listar_ingredientes():
    conexion = sqlite3.connect("empacuenta.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Ingredientes")
    ingredientes = cursor.fetchall()
    conexion.close()

    print("\nIngredientes:")
    for ingrediente in ingredientes:
        print(f"ID: {ingrediente[0]}, Nombre: {ingrediente[1]}, Precio: {ingrediente[2]}, Unidad: {ingrediente[3]}")

def listar_recetas():
    conexion = sqlite3.connect("empacuenta.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Recetas")
    recetas = cursor.fetchall()
    conexion.close()

    print("\nRecetas:")
    for receta in recetas:
        print(f"ID: {receta[0]}, Nombre: {receta[1]}, Costo Total: {receta[2]}")

def mostrar_receta_con_ingredientes(id_receta):
    conexion = sqlite3.connect("empacuenta.db")
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT r.nombre_empanada, i.nombre, ri.cantidad, i.precio_por_unidad
    FROM Recetas r
    JOIN Recetas_Ingredientes ri ON r.id_receta = ri.id_receta
    JOIN Ingredientes i ON ri.id_ingrediente = i.id_ingrediente
    WHERE r.id_receta = ?
    """, (id_receta,))
    datos = cursor.fetchall()
    conexion.close()

    print(f"\nReceta ID {id_receta}:")
    for dato in datos:
        nombre_receta, nombre_ingrediente, cantidad, precio = dato
        print(f"Ingrediente: {nombre_ingrediente}, Cantidad: {cantidad}, Precio Unitario: {precio}")

if __name__ == "__main__":
    listar_ingredientes()
    listar_recetas()
    mostrar_receta_con_ingredientes(1)
