class Aprendiz:#se crea una clases llamada aprendiz
    def __init__(self,fname,lname,email,id):#se inicializa el contrustor con sus respectivos parametros
        self.__fname=fname#se crea una variable de instancia con  su parametro
        self.__lname=lname#se crea una variable de instancia con  su parametro
        self.__email=email#se crea una variable de instancia con  su parametro
        self.__id=id#se crea una variable de instancia con  su parametro

    def nombreCompleto(self): #crea una funcion con su constructor
        return self.__fname+' '+self.__lname#se retorna la variable fname
