import sys#se importa el modulo sys
from sys import path#brinda acceso a algunas variables utilizadas o mantenidas por el intérprete 
#path.append('C:\\Users\\usuario\\Dropbox\\sena2022\\Trimestre4-06octubre-17diciembre\\MiPracticaPythonB\\modulos')
path.append('..\\MiPracticaPythonB\\modulos')#agrega un directorio llamado modulos que se encuentra en el directorio padre del directorio actual

# for p in sys.path:
#     print(p)
#path.append('..\\modules')
import modulo1#importa el modulo 1

x=[1,1,1,1,1]#se crea un lista 
y=[2,2,2,2,2]#se crea otra lista
print('--------')#imprime los caractares 
print(modulo1.__counter)#imprimir el valor de la variable de clase __counter en el módulo modulo1
zeroes = [0 for i in range(5)]#crea una lista llamada zeroes que contiene 5 elementos, todos iguales a cero
#devuelve el valor 0 para cada valor de i en el rango. Luego, estos valores se agregan a una lista usando la sintaxis de lista 
ones = [1 for i in range(5)]#crea una lista llamada ones  que contiene 5 elementos, todos iguales a uno
print(modulo1.suml(zeroes))# la función suml definida en el módulo "modulo1" y le pasa como argumento la lista zeroes
print(modulo1.prodl(ones))# la función prodl definida en el módulo "modulo1" y le pasa como argumento la variable ones intenta imprimir el resultado de la función
print(modulo1.suml(zeroes))#la función suml definida en el módulo "modulo1" y le pasa como argumento la lista zeroes
print(modulo1.prodl(ones)))# la función prodl definida en el módulo "modulo1" y le pasa como argumento la variable ones intenta imprimir el resultado de la función
print(modulo1.suml(x))#función suml definida en el módulo "modulo1" y le pasa como argumento la variable x
print(modulo1.prodl(y))#función suml definida en el móulo "modulo1" y le pasa como argumento la variable y

print(modulo1.__counter)#imprimir el valor de la variable de clase __counter en el módulo "modulo1"
