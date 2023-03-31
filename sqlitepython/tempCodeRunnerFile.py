import sqlite3#importa el modulo sqlite3
con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')#se conecta a la base de datos llamada conpython.db
print(type(con))#imprime el tipo de dato 
micursor=con.cursor()#crea un objeto para ejecutar consultas SQL en una base de datos
print(type(micursor))#imprime el tipo de dato del cursor
