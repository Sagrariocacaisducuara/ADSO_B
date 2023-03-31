import sqlite3# importa el modulo sqlite3

with sqlite3.connect('sqlitepython/conpython.db')as con:#se conecta a la base de datos llamada conpython.db
    micursor=con.cursor()#crea un objeto para ejecutar consultas SQL en una base de datos
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;"#definir una sentencia SQL para consultar en la base de datos
    #print(micursor.execute(sentencia).fetchall())#imprime una consulta SQL en la base de datos SQLite y con fetchall trae todos los registros que coinciden con la consulta

def miselect(conexion,tabla,campo,operador,dato): #crea una funcion que toma 5 parametros
    micursor=conexion.cursor()#crea un objeto para ejecutar consultas SQL en una base de datos
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"#definir una sentencia SQL para consultar en la base de datos
    print(sentencia)#imprime la consulta que se almaceno en la variable sentencia
    print(micursor.execute(sentencia).fetchall())#imprime una consulta SQL en la base de datos SQLite y con fetchall trae todos los registros que coinciden

#miselect(con,'alumno','email','=','dbrabon2@irs.gov')
#miselect(con,'alumno','id','<=',5)

def modificar(conexion,tabla,campo,dato,id):#crea una funcion que toma 5 parametros
    micursor=conexion.cursor()#crea un objeto para ejecutar consultas SQL en una base de datos
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id='{id}'"#definir una sentencia SQL para consultar en la base de datos
    micursor.execute(sentencia)#crea un objeto  de la variable sentencia para ejecutar consultas SQL en una base de datos
    con.commit()#confima una transaccion de la base de datos
    print('Modificación exitosa !!!!')#imprime la consulta 

#modificar(con,'alumno','nombre','Vegeta',1)
#DELETE FROM table_name WHERE condition;
def eliminar(conexion,tabla,campo,dato):#crea una funcion que toma 4 parametros
    micursor=conexion.cursor()#crea un objeto para ejecutar consultas SQL en una base de datos
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"#definir una sentencia SQL para consultar en la base de datos
    micursor.execute(sentencia)#crea un objeto  de la variable sentencia para ejecutar consultas SQL en una base de datos
    con.commit()#confima una transaccion de la base de datos
    print('Eliminación exitosa !!!!')#imprime la consulta 

eliminar(con,'alumno','id',3)#llama la cuncion con los campos de consulta 
