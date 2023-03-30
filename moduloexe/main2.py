from sys import path#importa la variable path desde el módulo sys

path.append('..\\MiPracticaPythonB\\modulos')# agrega una nueva ruta de búsqueda al final de la lista 
print(path)#imprime la lista de rutas de búsqueda que Python utilizará para encontrar módulos

import extra.iota#importa el módulo iota desde el paquete extra
import extra.good.best.tau# importa el módulo tau desde el subpaquete best del paquete good dentro del paquete extra

print(extra.iota.FunI())#mprime el resultado devuelto por esa función
print(extra.good.best.tau.FunT())#llama a la función FunT del módulo tau en el subpaquete best del paquete good dentro del paquete extra e imprime el resultado devuelto por esa función.
