#se crea una super clase llamada A1
class A1:
#se inicializa con su constructor y un atrubuto o parametro
    def __init__(self):
#es vacio
        pass
#se crea un metodo 
    def saludo(self):
#imprime el mensaje hola desde A1
        print('Hola desde A1')
#se crea otra super clase llamada A2
class A2:
#se inicializa con su constructor y un atrubuto o parametro
    def __init__(self):
#es vacio
        pass
#se crea un metodo 
    def saludo(self):
#imprime el mensaje hola desde A2
        print('Hola desde A2')

#se crea una clase hija
class B(A2,A1):
#se inicializa con su constructor y un atrubuto o parametro
    def __init__(self):
#es vacio
        pass
#se crea un metodo 
    def saludo(self):
#imprime el mensaje Hola desde B
        print('Hola desde B')
#se define el str
    def __str__(self):
#retorna la cadena de la clase hija
        return 'Soy un objeto de la clase B'
#la variable para la clase de (clase hija)
obj=B()
#imprime el medaje en la pantalla de la clase hija
print(obj.__str__())
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())
