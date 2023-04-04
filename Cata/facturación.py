import sqlite3
conec=sqlite3.connect("proyectosena.db")
cursor=conec.cursor()
tabla=input("Ingrese nombre de la tabla: ")
cursor.execute(f"PRAGMA table_info({tabla})")
columnas=cursor.fetchall()