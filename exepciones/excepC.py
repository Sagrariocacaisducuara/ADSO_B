def try_syntax(numerator, denominator):#realizar una división con el numerador y denominador proporcionados.
    try:#controla excepcione
        print(f'In the try block: {numerator}/{denominator}')#imprime un mensaje indicando que se está ejecutando el bloque try de la función try_syntax()
        result = numerator / denominator# realiza la operación de división entre numerator y denominator y se asigna el resultado a la variable result
    except ZeroDivisionError as zde:#se está especificando que si ocurre un error de división por cero
        print(zde)#imprime la variable zde
    else:#se ejecuta cuando no se ha producido ninguna excepción en el bloque try
        print('The result is:', result) #imprimir en la consola el resultado de la división realizada
        return result #devuelve el resultado de la división 
    finally:#El bloque se ejecuta independientemente de si se generó una excepción o no
        print('Exiting')#imprime exiting
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 0))#se intenta realizar la división 11/0 dentro del bloque try  Como el denominador es cero,
