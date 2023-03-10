class registrar():
    def __init__(self,id_usuario,nombre,edad,telefono,usuario,contraseña):
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
        self.usuario=usuario
        self.contraseña=contraseña
    
    def registrar(self,id_usuario,nombre,edad,telefono,usuario,contraseña):
        usuarioNuevo=registrar(id_usuario,nombre,edad,telefono,usuario,contraseña)
        self.usuario.append(usuarioNuevo)
class instructores():
    def __init__(self,credenciales):
        self.credenciales=credenciales

    def instructores(self,credenciales):
        nuevoInstructor=instructores(credenciales)
        self.credenciales.append(nuevoInstructor)

class asignatura():
    def __init__(self,id_asignatura,nombre_Asignatura,descripcion,instructor,cronograma):
        self.id_asignatura=id_asignatura
        self.nombre_Asignatura=nombre_Asignatura
        self.descripcion=descripcion
        self.instructor=instructor
        self.cronograma=cronograma
    def asignatura(self,id_asignatura,nombre_Asignatura, descripcion, instructor, cronograma):
        nuevaAsignatura=asignatura(id_asignatura,nombre_Asignatura,descripcion,instructor,cronograma)
        self.asignatura.append(nuevaAsignatura)

class estudiantes():
    def __init__(self, curso):
        self.curso=curso
    
    def estudiantes(self,curso):
        nuevosEstudiantes=estudiantes(curso)
        self.estudiantes.append(nuevosEstudiantes)


class inscripsiones():
    def __init__(self,id_inscripcion, detalles, requerimientos, datos):
        self.id_inscripcion=id_inscripcion
        self.detalles=detalles
        self.requerimientos=requerimientos
        self.datos=datos
    
    def inscripsiones(self,id_inscripcion, detalles, requerimientos, datos):
        nuevasInscripciones=inscripsiones(id_inscripcion,detalles,requerimientos,datos)
        self.inscripsiones.append(nuevasInscripciones)

class curso():
    def __init__(self, id_curso, descripcion, datos, nivel_anual):
        self.id_curso=id_curso
        self.descripcion=descripcion
        self.datos=datos
        self.nivel_anual=nivel_anual

    def curso(self,id_curso,descripcion, datos, nivel_anual):
        nuevoCurso=curso(id_curso, descripcion, datos, nivel_anual)
        self.curso.append(nuevoCurso)

class transacion():
    def __init__(self,id_transacion, detalles, datos):
        self.id_transacion=id_transacion
        self.detalles=detalles
        self.datos=datos
    def transacion(self,id_transacion, detalles, datos):
        transacionNueva=transacion(self,id_transacion, detalles, datos)
        self.transacion.append(transacionNueva)


usuario1=registrar(223,'maria',12,2345,'maria1','jhchb')
print('id_usuario: ',usuario1.id_usuario)
print('nombre: ',usuario1.nombre)
print('edad: ',usuario1.edad)
print('telefono: ',usuario1.telefono)
print('usuario: ',usuario1.usuario)
print('contraseña: ',usuario1.contraseña)

instructor1=instructores('alfonso')
print('credenciales: ',instructor1.credenciales)

asignatura1=asignatura(23445,'matematicas', 'intelectual', 'Sebastian Rodriguez', 1234)
print('id_Asignatura: ',asignatura1.id_asignatura)
print('descripcion: ',asignatura1.descripcion)
print('instructor: ',asignatura1.instructor)
print('cronograma: ',asignatura1.cronograma)

estudiantes1=estudiantes(134)
print('nuevoCurso: ',estudiantes1.curso)

inscripsiones1=inscripsiones(2325,'fvhbdhf','jfdhbdf','jfdvdkm')
print('id_inscripcion: ',inscripsiones1.id_inscripcion)
print('detalles: ',inscripsiones1.detalles)
print('requerimientos: ',inscripsiones1.requerimientos)
print('datos: ',inscripsiones1.datos)

curso1=curso(75443,'emprendedor',12345,45678)
print('id_curso: ',curso1.id_curso)
print('descripcion: ',curso1.descripcion)
print('datos: ',curso1.datos)
print('nivel_anual',curso1.nivel_anual)

transacion1=transacion(978896,'kfjndjv',4556)
print('id_transacion: ',transacion1.id_transacion)
print('detalles: ',transacion1.detalles)
print('datos: ',transacion1.datos)
