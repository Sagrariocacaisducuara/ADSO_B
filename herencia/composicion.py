#se crea una clase padre llamada aprendiz
class Aprendiz:
#se inicializa con su constructor y un atrubuto o parametro
    def __init__(self,nombre):
#se crea una variable de instancia
        self.__nombre=nombre
#se crea una variable de instacia llamada curso con una lista vacia
        self.__cursos=[]
#se crea un metodo llamado agregarCurso con sus respectivos parametros
    def agregarCurso(self,titulo):
#se ustiliza el metodo append para agregar una nuevo metodo llamado cursos
        self.__cursos.append(titulo)
#se utiliza el metodo get y se utiliza el argunto sefl
    def getTitulo(self):
#se retorna la la variable titulo
        return self.__cursos
#se crea una clase hija llamada curso
class Curso:
#inicializa con su constructor y un atrubuto o parametro
    def __init__(self,titulo):
#se crea una variable de instacia llamada curso con una lista vacia
        self.__titulo=titulo
#self le agregamos el titulo para indicar que pretenece a esta clase
    def getTitulo(self):
#retorna el metodo get.titulo
        return self.__titulo
#se crea un objeto de la calse aprendiz para llamar el objeto
a=Aprendiz('Martha')
#se crea otro objeto de la clase curso para llamar el objeto
c1=Curso('Python Intermedio')
#se crea otro objeto de la clase curso para llamar el objeto
c2=Curso('Python Basico')
#se crea otro objeto de la clase curso para llamar el objeto
c3=Curso('Introduccion a Java')
#se crea otro objeto llamdo a de la clase curso para llamar el objeto
a.agregarCurso(c1)
#se crea otro objeto de la clase curso para llamar el objeto
a.agregarCurso(c2)
#se crea otro objeto de la clase curso para llamar el objeto
a.agregarCurso(c3)
#imprime el objeto de getCurso en la consola
print(a.getCursos())

#recorre el curso hasta getCurso
for curso in a.getCursos():
#imprime la clase curso la lista get.Curso
    print(curso.getTitulo())
