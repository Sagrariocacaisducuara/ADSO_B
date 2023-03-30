import csv#se importa el modulo csv
diccio=[#se crea un diccionario
    {'name':'Alice','age':18},#clave-valor del diccionario
    {'name':'Bob','age':19},#clave-valor del diccionario
    {'name':'John','age':17}#clave-valor del diccionario
]
header=['name','age']#se está definiendo una lista llamada header que contiene dos elementos

with open('archivos/people.csv','w') as csvfile:#se está abriendo un archivo llamado people.csv en modo de escritura ('w') y se está asignando a la variable csvfile
    writer=csv.DictWriter(csvfile,fieldnames=header)#se está creando un objeto DictWriter de la biblioteca CSV en Python llamado writer
    writer.writeheader() #se está escribiendo la fila de encabezado en el archivo CSV utilizando el objeto DictWriter previamente definido.
    writer.writerows(diccio)#se están escribiendo múltiples filas en el archivo CSV utilizando el objeto DictWriter previamente definido.
