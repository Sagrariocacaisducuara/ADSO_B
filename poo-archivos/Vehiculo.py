class Vehiculo:#se crea la case Vehiculo
    def __init__(self,placa,conductor):#se inicialoiza su constructor con sus respectivos atributos
        self.__placa=placa# se asigna el valor a el atribito placa
        self.__conductor=conductor# se asigna el valor a el atribito conductor
    def getConductor(self):#define un metodo en la clase
        return self.__conductor#se retorna el valor del atriburo conductor
    def getPlaca(self)::#define un metodo en la clase
        return self.__placa#se retorna el valor del atriburo placa
