
#un grupo tienes varias materias
#cada grupo oferta un tiraje de materias 
#el alumno se agrega desde el grupo



class GrupoPrueba():
	def __init__(self, nombreG, salon, cupo):
		self.nombreG=nombreG
		self.salon=salon
		self.cupo=cupo
		self.espacio=True
		self.materias=[]
		self.Alumnos=[]
	# 
	def __str__(self):
		str_id = "Grupo: {0} \nSalon: {1} \nMaterias: {2} \nAlumnos: {3} "
		return str_id.format(self.nombreG, self.salon, ", ".join([asignatura.nomAsig for asignatura in self.materias]), ", ".join([alumno.nombre for alumno in self.Alumnos]))


	def insertarMateria(self, materia):
		self.materias.append(materia)
		print('Materia:', str(materia), 'inscrita')

	def eliminarMateria(self, materia):
			self.materias.remove(materia)
			print('Materia;', str(materia), 'removida')

	#valida el cupo y agrega al nuevo alumno
	def insertarAlumno(self, alumno):
		self.verificarCupo()
		if self.espacio==True:
			self.Alumnos.append(alumno)
			print('alumno:',str(alumno), 'agregado')
		else:
			print("el cupo se ha agotado, el alumno:",str(alumno), "no se ha incrito")

	def eliminarAlumno(self, alumno):
		self.Alumnos.remove(alumno)
		print('alumno',str(alumno), 'removido')
	
	#metodo para validar el cupo en el grupo
	def verificarCupo(self):
		cup=self.cupo
		if cup>len(self.Alumnos):
			self.espacio=True
			tmp=cup-len(self.Alumnos)
			print("Espacio disponible para: ", tmp, "alumnos")
		else: 
			self.espacio=False


class Asignatura():

	def __init__(self, nomAsig):
		self.nomAsig = nomAsig

	def __str__(self):
		return self.nomAsig


class Alumno():
	def __init__(self, nombre, edad, matricula):
		self.nombre=nombre
		self.edad=edad
		self.matricula=matricula

	def __str__(self):
		return self.nombre


#------------pruebas-------------
ciencias=Asignatura("Ciencias")
mate=Asignatura("Matematicas")
print("-------------asdfghjkl------------")
g5=GrupoPrueba("segundo grupo", "cc2", 6)
g5.insertarMateria(ciencias)
g5.insertarMateria(mate)
a1=Alumno("Fers", 22, 12345)
a2=Alumno("Ruben", 23, 1234567)
g5.insertarAlumno(a1)
g5.insertarAlumno(a2)
g5.verificarCupo()
g5.eliminarMateria(mate)
print(g5)
g5.verificarCupo()