#def divisores(num):
#     for i in range(num):
#         if num%i==0:
#             print(i,' es divisor')

# try:
#     divisores(19)
# except:

def divisores(num):#define una función llamada divisores que toma un parámetro num

    if type(num)!=int:#verifica si el tipo de datos del parámetro num es diferente de int 
        print('Solo trabaja con numeros')#se imprime en la consola
    else:#es lo contrario de if
        try:#indican que si el parámetro num es un número entero válido, el código dentro del bloque try se ejecutará
            for i in range(1,num):#crea un ciclo que iterará a través de una secuencia de números desde 1 hasta num - 1
                if num%i==0:#verifica si el número i es un divisor de num
                    print(i,' es divisor')#mprime en pantalla el número i y el mensaje es divisor 
        except ZeroDivisionError:#se utiliza para manejar la excepción que se produce cuando el valor de num es igual a cero
            print('Indeterminacion')#imprime indeterminacion
        except TypeError:#maneja la excepción que se produce cuando el valor de num no es un entero
            print('No ingreso un numero')#imprime no ingreso un numero
        except: #maneja cualquier otra excepción que no haya sido manejada por los bloques except anteriores
            print('Error no determinado')#imprime error no determinada

divisores([])#se producirá una excepción de tipo TypeError en la
print('El programa continua desde aqui') #imprime el programa continua desde aqui
