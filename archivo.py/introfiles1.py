with open ('archivos/basico1.txt','w') as flujo:#se está abriendo un archivo llamado basico1.txt en modo de escritura ('w') y se está asignando a la variable flujo
    flujo.write('Escribir o crear el archivo \n')#escribe la cadena de caracteres en un archivo que se ha abierto en modo de escritura y que está representado por la variable flujo

with open ('archivos/basico1.txt','a') as flujo:#abre un archivo en el directorio en modo de escritura y lo asigna a la variable flujo
    flujo.write('esta es una linea nueva\n')#escribe la cadena de caracteres en el archivo representado por la variable flujo que se ha abierto en modo de escritura 
