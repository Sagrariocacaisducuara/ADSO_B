class Conductor:#se crea la clase persona
    def __init__(self,nombre,documento):#se inicialoiza su constructor con sus respectivos atributos
        self.__nombre=nombre# se asigna el valor a el atributo mnonbre
        self.__documento=documentose asigna el valor a el atributo documento
    def getNombre(self):#define un metodo en la clase #devuelve el valor del atriburo nombre
        return self.__nombre#retorna el valor del atriburo nombre
    def getDocumento(self):#define un metodo en la clase para el valor del atributo documento
        return self.__documento#retorna el valor del atriburo documento
