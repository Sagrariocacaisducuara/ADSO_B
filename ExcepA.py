# el try es un bloque de codigo al momento de haser una comprobacion de errores
try:
    #print(1/1))
#es un generador de errores
    raise SyntaxError
#se ejecutara cuando el bloque try falle debido a un error
except SyntaxError:
#imprime los argumentos que se encuentren dentro de los parentecis y comillas
    print('Cierra el parentesis')
