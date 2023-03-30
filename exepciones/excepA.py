try: #para controlar excepciones
    #print(1/1))
    raise SyntaxError#generar manualmente una excepción
except SyntaxError:#se genera en el bloque try anterior.
    print('Cierra el parentesis')#imprime cierra paretesis
