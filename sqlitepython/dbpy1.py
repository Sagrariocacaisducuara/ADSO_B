import sqlite3#importa el modulo sqlite3
with sqlite3.connect('sqlitepython/conpython.db')as con: #se conecta a la base de datos llamada conpython.db
    micursor=con.cursor()#crea un objeto para ejecutar consultas SQL en una base de datos
    sentencia="SELECT nombre,apellido FROM alumno;"# definir una sentencia SQL 
    print(micursor.execute(sentencia).fetchmany(10))imprime la consulta SQL de la base de datos

#print()
