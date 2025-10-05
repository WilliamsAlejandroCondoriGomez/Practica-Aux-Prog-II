class Persona:
    def __init__(self, nombre, ci):
        self.nombre = nombre
        self.ci = ci
    def mostrar(self):
        print(f"Nombre: {self.nombre}, CI: {self.ci}")
class Estudiante(Persona):
    def __init__(self, nombre, ci, carrera):
        super().__init__(nombre, ci)
        self.carrera = carrera
    def mostrar(self):
        super().mostrar()
        print(f"Carrera: {self.carrera}")
class Docente(Persona):
    def __init__(self, nombre, ci, materia):
        super().__init__(nombre, ci)
        self.materia = materia
    def mostrar(self):
        super().mostrar()
        print(f"Materia: {self.materia}")
e1 = Estudiante("Luis", "1234567", "Informática")
d1 = Docente("Carlos", "7654321", "Programación II")
e1.mostrar()
d1.mostrar()