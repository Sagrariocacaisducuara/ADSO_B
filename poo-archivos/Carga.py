from Vehiculo import *#se importa el modulo vehiculo 
class Carga(Vehiculo):#se crea una clase llamada carga que viene de otra clase vehiculo
    def __init__(self,placa,conductor,capacidad,ejes):#se ninializa su constrcutor con 5 parametros
        Vehiculo.__init__(self,placa,conductor)#se instancia la clase vehiculo
        self.__capacidad=capacidad#se crea una variable de instancia
        self.__ejes=ejes    #se crea una variable de instancia
    def getCapacidad(self):#se crea el metodo getCapacidad
        return self.__capacidad #se retorna la variable capacidad
    def getEjes(self):#se crea el metodo getEjes
        return self.__ejes#se retorna la variable ejes
