class Persona:#se crea la clase persona
    
    def __init__(self,id,nombre,apellido,email):#se inicialoiza su constructor con sus respectivos atributos
        self.__id=id # se asigna el valor a el atributo privado id 
        self.__nombre=nombre# se asigna el valor a el atributo nombre
        self.__apellido=apellido# se asigna el valor a el atributo apellido
        self.__email=email# se asigna el valor a el atributo email

    def getNombre(self): #define un metodo en la clase  s
        return self.__nombre#devuelve el valor del atriburo nombre
    
    def setNombre(self, nombre):#define un metodo en la clase para el valor del atributo nombre
        self.__nombre=nombre#asigna el valor al tributo nombre 

    def getNombreCompleto(self):#define un metodo en la clase
        return self.__nombre+' '+self.__apellido#retorna el atributo completo de un objeto de la clase persona 
