class Persona:#cre crea la clase persona 
    nacionalidad='Colombia'#asigna un  un valor a la variable nacinalidad
    def __init__(self,nombre,documento):#se inicialoiza su constructor con sus respectivos atributos
        self.__nombre=nombre# se asigna el valor a el atributo privado nombre
        self.__documento=documento# se asigna el valor a el atributo documento
        print('Activando constructor')#imprime activando constructor

    def getNombre(self):#define un metodo en la clase  
        return self.__nombre#devuelve el valor del atriburo nombre
    
    def setNombre(self, nombre):#define un metodo en la clase para el valor del atributo nombre
        self.__nombre=nombre#asigna el valor al tributo nombre 

    def metodo(self,mail):#define un metodo en la clase para el valor del atributo mail
        self.__mail=mail#asigna el valor al tributo nombre 
        #print('Soy un método')#imprime soy un metodo



ob=Persona('Ana',12345)#crea un objeto de la clase Persona con los atributos nombre y id 
ob.mail='ana@mail.com'#asignar un valor al atributo mail del objeto ob de la clase Persona
print(ob.mail)#imprime el objeto mail
ob1=Persona('Luis',54321)#crea un objeto de la clase Persona con los atributos nombre y id 
print(ob.nacionalidad)imprimi el valor del atributo nacionalidad del objeto ob de la clase Persona
print(ob1.nacionalidad)imprimi el valor del atributo nacionalidad del objeto ob de la clase Persona
print(Persona.nacionalidad)imprimi el valor del atributo nacionalidad de la clase "Persona"

print(ob.getNombre())#mprimir el valor retornado por el método getNombre() del objeto ob de la clase Persona
ob.setNombre('Maria')#llamar al método setNombre() del objeto ob de la clase Persona, y así establecer un nuevo valor para el atributo nombre
print(ob.getNombre())#imprimir el valor actualizado del atributo nombre del objeto ob de la clase Persona
#ob.metodo()
#print(type(ob))

cadena="SENA"#asignar la cadena de caracteres SENA a la variable cadena
print(cadena.lower())#imprimir la variable cadena en minúsculas
print(type(cadena))#para imprimir el tipo de dato de la variable cadena.
