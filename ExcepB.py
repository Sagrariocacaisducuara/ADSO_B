#se crea una variable para crear una tupla y almacenar unos valores en  ella
values = (1, 0)
#x,y=19,30
#print(divmod(10,3))

#el try es un bloque de codigo al momento de haser una comprobacion de errores
try:
#son dos variables en un sola linea de codigo y y divmod es el residulo de una divicion 
    q, r = divmod(*values)
    #print('q=',q)
#realizara un print,la f es temples iterales esto combina variables de numero con cadenas de texto
    print(f'q={q}')
    print(f'r={r}')
##se ejecutara cuando el bloque try falle debido a un error
except (ZeroDivisionError, TypeError) as e:
##imprime los argumentos que se encuentren dentro de los parentecis y comillas
    print(type(e), e)
