import sqlite3

def verificar_tablas():
    conexion = sqlite3.connect("empacuenta.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()
    if tablas:
        print("Tablas existentes en la base de datos:")
        for tabla in tablas:
            print(f"- {tabla[0]}")
    else:
        print("No hay tablas en la base de datos.")
    conexion.close()

if __name__ == "__main__":
    verificar_tablas()
