import sqlite3

conexion = sqlite3.connect("empacuenta.db")
cursor = conexion.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
conexion.close()

print("Tablas en la base de datos:")
for tabla in tablas:
    print(tabla[0])
