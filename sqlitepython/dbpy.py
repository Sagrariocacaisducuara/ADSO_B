import sqlite3# se importa el modulo sqlite3
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')
con=sqlite3.connect('sqlitepython/conpython.db')#se crea una variable de instancia y usamos .connect para conactar con el sqlite2 y le damos una ruta en este caso es relativa
print(type(con))#imprimos el tipo de dato es
micursor=con.cursor()#es otra variable d estacia llamada mi cursor y con el .cursor se le da sentencias 
print(type(micursor))#imprimimos el tipo de datos es
sentencia="SELECT * from alumno;"#sentencias de sqlite que se llaman con strig
micursor.execute(sentencia)#ejecuta la sentencia
for fila in micursor.fetchall():#recorre y itera la sentencia y con el fetchall seleciona todos los datos
    print(fila[0])#imprime la posisicon 0 de los datos
    print(fila[1])#imprime la posisicon 1 de los datos
    print(fila[2])#imprime la posisicon 2 de los datos
    print(fila[3])#imprime la posisicon 3 de los datos
    print('-'*50)#imprime 50datos
