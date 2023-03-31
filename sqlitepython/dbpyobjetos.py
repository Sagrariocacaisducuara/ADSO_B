from Persona import * #se importa todo de la classe persona
import sqlite3#se importa el modulo sqlite3
lista=[]#crea una lista vacia 
personas=[]#se crea otra lista vacia 
with sqlite3.connect('sqlitepython/conpython.db')as con:##se conecta a la base de datos llamada conpython.db
    micursor=con.cursor()#crea un objeto para ejecutar consultas SQL en una base de datos
    sentencia="SELECT * FROM alumno;"#defini una sentencia SQL para consultar en la base de datos
    lista=micursor.execute(sentencia).fetchall()ejecuta un consulta y almacena los datos en una lista de tuplas 
#print(lista)
for fila in lista:#recorre la lista que contiene las consultas SQL
    id=fila[0]#asigna el valor del primer elemento de la lista 
    nombre=fila[1]#asigna el valor del segundo elemento de la lista 
    apellido=fila[2]#asigna el valor del tercer elemento de la lista 
    email=fila[3]#asigna el valor del cuarto elemento de la lista 
    ob=Persona(id,nombre,apellido,email)crea un objeto de la clase persona y lo asigna en la variable ob
    personas.append(ob)#agrega un objeto a la lista persona 

for objeto in personas:#recorre la lista persona 
    print(objeto.getNombreCompleto())#imprime el resultado al llamar el metodo getNombreCompleto en el objeto de la clase
