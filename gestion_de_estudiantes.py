class registrar():
    def __init__(self,id_usuario,nombre,edad,telefono,usuario,contraseña):
        self.__id_usuario=id_usuario
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
        self.usuario=usuario
        self.contraseña=contraseña

class instructores():
    def __init__(self,credenciales):
        self.__credenciales=credenciales

class asignatura():
    def __init__(self,id_asignatura,nombre_Asignatura,descipcion,instructor,cronograma):
        self.__id_asignatura=id_asignatura
        self.nombre_Asignatura=nombre_Asignatura
        self.descipcion=descipcion
        self.instructor=instructor
        self.crenograma=cronograma
    def getInformacion(self, id_asignarura, nombre_asignatura, descripcio, instructor, cronograma):
        return self.__id_asignatura, self.nombre_Asignatura, self.descipcion, self.instructor, self.cronograma

class estudiantes():
    def __init__(self, curso):
        self.__curso=curso


    