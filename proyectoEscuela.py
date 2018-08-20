
#un grupo tienes varias materias
#cada grupo oferta un tiraje de materias 
#el alumno se agrega desde el grupo

class Grupo():
    def __init__(self, nombreG, salon, cupo):
        self.nombreG=nombreG
        self.salon=salon
        self.cupo=int(cupo)
        self.materias=[]
        self.alumnos=[]

    def __str__(self):
        str_id = "Grupo: {0} \nSalon: {1} \nMaterias: {2} \nAlumnos: {3} \nCupo disponible: {4}"
        return str_id.format(self.nombreG, self.salon, ", ".join([asignatura.nomAsig for asignatura in self.materias]), len(self.alumnos), self.cupo-len(self.alumnos))
    
    def insertar_materia(self, materia):
        if not self._verificar_duplicados(materia):
            self.materias.append(materia)
            print('Materia:', str(materia), 'inscrita')
        else:
            print('La materia: ',str(materia),'ya se encuentra inscrita')

    def eliminar_materia(self, materia):
            self.materias.remove(materia)
            print('Materia;', str(materia), 'removida')

    def _verificar_duplicados(self, materia):
        if materia in self.materias:
            return True

        return False

    #valida el cupo y agrega al nuevo alumno
    def insertar_alumno(self, alumno):
        if self.verificar_cupo() and not self._alumno_duplicado(alumno):
            self.alumnos.append(alumno)
            print('alumno:',str(alumno), 'agregado')
        else:
            print("El alumno:",str(alumno), "no se ha incrito")

    def eliminar_alumno(self, alumno):
        self.alumnos.remove(alumno)
        print('alumno',str(alumno), 'removido')

    def imprimir_alumnos(self):
        for i in self.alumnos:
            print(i)

    def _alumno_duplicado(self, alumno):
        if alumno in self.alumnos:
            return True

        return False

    #metodo para validar el cupo en el grupo
    def verificar_cupo(self):
        if self.cupo > len(self.alumnos):
            print("Espacio disponible para: ", self.cupo-len(self.alumnos), "alumnos")
            return True
        
        return False

    def modificar_cupo(self, cupo):
        tmp=self.cupo
        self.cupo=cupo
        print('se ha modificado el cupo del grupo de:', tmp, 'a', self.cupo)


class Asignatura():

    def __init__(self, nomAsig):
        self.nomAsig = nomAsig

    def __str__(self):
        return self.nomAsig


class Alumno():
    def __init__(self, nombre, edad, matricula):
        self.nombre=nombre
        self.edad=int(edad)
        self.matricula=matricula

    def __str__(self):
        return self.nombre


"""#------------NOTAS Y PRUEBAS-------------#
ciencias=Asignatura("Ciencias")
mate=Asignatura("Matematicas")
print("-------------asdfghjkl------------")
g5=Grupo("segundo grupo", "cc2", 6)
g5.insertar_materia(ciencias)
g5.insertar_materia(mate)
a1=Alumno("Fers", 22, 12345)
a2=Alumno("Ruben", 23, 1234567)
a3=Alumno("Cristo", 27, 234235)
g5.insertar_alumno(a1)
g5.insertar_alumno(a2)
g5.insertar_alumno(a2)
g5.verificar_cupo()
g5.insertar_materia(mate)
print(g5)
g5.imprimir_alumnos()
g5.modificar_cupo(10)
g5.insertar_alumno(a3)
print(g5)"""


"""no se puede insertar un alumno dos veces, ni materias
funcion imnprimir alumnos 
poder cambiar el cupo 
funcion imprimir  str solo num y cupo 
como ejecutar pruebas en python

    code review
tab != tienen que ser 4 espacios
nombres de metodos separeados con _
atribuitos nombres con minusculas
funciones dentro de clases solo un salto
clases dos saltos 
separar tmp == oasid



"""

