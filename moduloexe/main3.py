from sys import path#importa la variable path desde el módulo sys de la biblioteca estándar de Python.

path.append('..\\MiPracticaPythonB\\modulozip\\extrapack.zip')# agrega una nueva ruta de búsqueda al final de la lista de rutas de búsqueda del módulo de Python

import extra.good.best.sigma as sig #importa el módulo sigma del subpaquete best del paquete good dentro del paquete extra y lo asigna a un alias sig
import extra.good.alpha as alp#importa el módulo alpha del paquete good dentro del paquete extra y lo asigna a un alias alp
from extra.iota import FunI#mporta la función FunI directamente desde el módulo iota del paquete extra

from extra.good.beta import FunB#importa la función FunB directamente desde el módulo beta del paquete good dentro del paquete extra

print(sig.FunS())#muestra el resultado en la consola
print(alp.FunA())#muestra el resultado en la consola.
print(FunI())#muestra el resultado en la consola.
print(FunB())#muestra el resultado en la consola.
