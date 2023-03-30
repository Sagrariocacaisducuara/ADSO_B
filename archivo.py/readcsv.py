from Aprendiz import *# importar todas las funciones, clases y variables definidas en el archivo Aprendiz.py
import csv#se importa el modulo csv
listaAprendices=[]#se crea una lista vacia
with open('C:\\Users\\usuario\\Documents\\01-SENA\\NetAcademy2023\\2693629.csv') as csvDataFile:
#se utiliza para abrir un archivo CSV con la ruta de archivo especificada y crear un objeto de archivo CSV csvDataFile que se utiliza para leer los datos del archivo.

#with open('files/people.csv') as csvDataFile:
#with open('https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html/addresses') as csvDataFile:
    csvReader=csv.reader(csvDataFile)#crea un objeto csv.reader que se puede utilizar para leer los datos del archivo CSV
    #print(csvReader)
    for row in csvReader:#crea un bucle for querecorre cada fila del archivo CSV que se ha abierto previamente y que se ha leído utilizando el objeto csv.reader
        apr=Aprendiz(row[0],row[1],row[2],row[3])#crea un objeto de la clase "Aprendiz" utilizando los valores de la lista que representa una fila del archivo CSV.
        listaAprendices.append(apr)#agrega el objeto apr que es una instancia de la clase Aprendiz a una lista llamada listaAprendices
        #print(row)
        #print('first name:',row[0])
        #print('last name:',row[1])
        #print('email:',row[2])
        #print('id:',row[3])
print(listaAprendices)#imprime la listAprendices 
for apr in listaAprendices: #recorre cada elemento en la lista listaAprendices y asigna temporalmente cada elemento a la variable apr
    print(apr.nombreCompleto())#imprime el resultado de llamar al método nombreCompleto() del objeto apr

