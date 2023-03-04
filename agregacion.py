#se crea una clase 
class Curso:
#se inicializa con su constructor y un atrubuto o parametro
    def __init__(self,titulo):
# se crea una variable de instancia
        self.__titulo=titulo
#se utiliza el metodo get y se utiliza el argunto sefl
    def getTitulo(self):
#se retorna la variable titulo 
        return self.__titulo
#se crea una clase hija llamada Aprendiz
class Aprendiz:
#se inicializa con su constructor y un atrubuto o parametro en este caso nombre
    def __init__(self,nombre):
#se crea una variable de instancia
        self.__nombre=nombre
#se crea una variable de instacia llamada curso con una lista vacia
        self.__cursos=[]
#se crea un metodo con sus respectivos argumentos
    def agregarCurso(self,nombreCursito):
#se crea una variable de instancia
        cursito=Curso(nombreCursito)
#se ustiliza el metodo append para agregar una nuevo metodo llamado agragarCurso
        self.__cursos.append(cursito)
#se utiliza el metodo get y se utiliza el argunto sefl
    def getCursos(self):
#se retorna la variable cursos para
        return self.__cursos
#creamos un objeto llamado ap de la clase aprendiz y le asignamos el nombre de sofia
ap=Aprendiz('Sofia')
#se crear otro objeto igualmete llamado con el metodo de agragar curso y de este le daremos una cadena llamada python basico 
ap.agregarCurso('Python Basico')
#se crear otro objeto igualmete llamado con el metodo de agragar curso y de este le daremos una cadena llamada python intermedio
ap.agregarCurso('Python Intermedio')
#se inicia un bucle for con la variable c y a esto le asignamos el objeto ap.getcursos
for c in ap.getCursos():
#imprimimos la variable c del for para imprimir get.titulo
    print(c.getTitulo())
