import unittest
from proyectoEscuela import *

class test_grupo(unittest.TestCase):
	def test_crear_objetos(self):
		a21=Alumno('brenda', 22, 'kadfhkdf')
		ciencias=Asignatura(14234)
		mate=Asignatura('mate')
		g1=Grupo('primer grupo', 123, 13)
		self.assertTrue(Grupo)
		self.assertTrue(Asignatura)
		self.assertTrue(Alumno)

	def test_agregar_al_grupo(self):
		a21=Alumno('Fers', 22, 81732)
		mate=Asignatura('mate')
		g1=Grupo('primer grupo', 123, 13)
		g1.insertar_materia(mate)
		g1.insertar_materia(mate)
		g1.insertar_materia(a21)
		g1.insertar_alumno(a21)
		g1.insertar_alumno(a21)
		self.assertTrue(g1.alumnos)
		self.assertTrue(g1.materias)

	def test_eliminar_objetos(self):
		a21=Alumno('Fers', 22, 81732)
		g1=Grupo('primer grupo', 'cc2', 2834)
		mate=Asignatura('Matematicas')
		g1.insertar_materia(mate)
		g1.eliminar_materia(mate)
		g1.insertar_alumno(a21)
		g1.eliminar_alumno(a21)
		self.assertFalse(g1.materias)
		self.assertFalse(g1.alumnos)

if __name__ =='__main':
	unittest.main()