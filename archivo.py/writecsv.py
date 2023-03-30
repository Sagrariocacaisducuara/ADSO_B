import csv #se importa el modulo csv
header=['Fruit','Price']#se está creando una lista llamada header que contiene los nombres de las columnas que se utilizarán en el archivo CSV.
rows=[['Apple',1200], #se está creando una lista de listas llamada "rows" que contiene los datos que se escribirán en el archivo CSV.
      ['Berry',2000], #se está agregando una nueva lista de datos a la lista
      ['Lemon',1000], #se está agregando una nueva lista de datos a la lista
      ['Melon',3000],#se está agregando una nueva lista de datos a la lista
      ['Grapes',4000],#se está agregando una nueva lista de datos a la lista
      ['Pear',2000]]  #se está agregando una nueva lista de datos a la lista

with open ('archivos/example.csv','w') as csvfile:#se está abriendo un archivo llamado example.csv en modo de escritura ('w') y se está asignando a la variable csvfile
    csvwriter=csv.writer(csvfile)#se está creando un objeto csvwriter de la clase csv.writer
    csvwriter.writerow(header)#se está utilizando el objeto "csvwriter" creado anteriormente
    csvwriter.writerows(rows) #se está utilizando el objeto "csvwriter" creado anteriormente
