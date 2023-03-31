from Carga import *#importa todos los nombres definidos en el módulo o archivo Carga
from Conductor import *#importa todos los nombres definidos en el módulo o archivo conductor
# c1=Conductor('Luis',12345)
# carga1=Carga('aaa-123',c1,5,2)
# print(carga1)
nomConductor=input('Ingrese nombre del conductor')le pedi al usuario que ingrese el nombre del conductor y asignar el valor ingresado a una variable llamada nomConductor
docConductor=int(input('Ingrese documento del conductor'))le pedi al usuario que ingrese el documento del conductor y asignar el valor ingresado a una variable llamada docConductor
placa=input('ingrese placa')le pedi al usuario que ingrese la placa del conductor y asignar el valor ingresado a una variable llamada placa
capacidad=input('ingrese capacidad en toneladas')le pedi al usuario que ingrese la capacidad y asignar el valor ingresado a una variable llamada capacidad
ejes=input('ingrese numero de ejes')le pedial usuario que ingrese el numero de ejes y asignar el valor ingresado a una variable llamada ejes
c1=Conductor(nomConductor,docConductor)#crea una instancia de la clase Conductor y asigna esa instancia a la variable c1
obCarga=Carga(placa,c1,capacidad,ejes) #crea un objeto de la clase Carga y se está asignando a la variable obCarga
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento())#se está llamando a dos métodos de la instancia de la clase Carga almacenada en la variable obCarga

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes())#lama al método getPlaca() de la instancia de la clase Carga almacenada en obCarga para obtener la placa del vehículo de carga que se concatena con una coma (',') y la variable cadConductor

with open('poo-archivos/listado.txt','a') as flujo:# se está abriendo un archivo de texto llamado listado.txt
    flujo.write(cadCarga+'\n')#se está escribiendo una cadena de caracteres en el archivo de texto asociado al objeto flujo
