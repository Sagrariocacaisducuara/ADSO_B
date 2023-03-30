values = (1, 0)#se crea una tupla llamada values que contiene los valores enteros 1 y .
#x,y=19,30
#print(divmod(10,3))
try:#controla excepciones
    q, r = divmod(*values)#toma dos argumentos y devuelve un par de valores el resultado de la división y el residuo de esa división. 
    #print('q=',q)
    print(f'q={q}')#imprime el valor de la variable q
    print(f'r={r}')#imprime el valor de la variable r
except (ZeroDivisionError, TypeError) as e:#se utiliza para manejar excepciones en caso de que se produzcan errores al ejecutar el código que está dentro del bloque try
    print(type(e), e)#mprimirá el tipo de excepción y el mensaje de la excepción que se ha capturado en el bloque except
