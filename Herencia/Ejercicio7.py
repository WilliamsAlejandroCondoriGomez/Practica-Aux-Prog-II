class Persona:
    def __init__(self, nombre, paterno, materno, edad):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Apellido Paterno:", self.paterno)
        print("Apellido Materno:", self.materno)
        print("Edad:", self.edad)
class Docente(Persona):
    def __init__(self, nombre, paterno, materno, edad, sueldo, reg_profesional):
        super().__init__(nombre, paterno, materno, edad)
        self.sueldo = sueldo
        self.reg_profesional = reg_profesional
    def mostrar(self):
        super().mostrar()
        print("Sueldo:", self.sueldo)
        print("Registro Profesional:", self.reg_profesional)
class Estudiante(Persona):
    def __init__(self, nombre, paterno, materno, edad, ru, matricula):
        super().__init__(nombre, paterno, materno, edad)
        self.ru = ru
        self.matricula = matricula
    def mostrar(self):
        super().mostrar()
        print("RU:", self.ru)
        print("Matrícula:", self.matricula)
    def modificar_edad(self, nueva):
        self.edad = nueva
    def misma_edad(self, docente):
        return self.edad == docente.edad
    def promedio(self, otro_estudiante):
        return (self.edad + otro_estudiante.edad) / 2
est1 = Estudiante("Ana", "Gomez", "Lopez", 20, "RU123", "MAT2025")
est2 = Estudiante("Luis", "Perez", "Quispe", 22, "RU456", "MAT2026")
doc1 = Docente("Carlos", "Rojas", "Mamani", 22, 5000.0, "REG789")
print("Estudiante 1:")
est1.mostrar()
print("\nEstudiante 2:")
est2.mostrar()
print("\nDocente:")
doc1.mostrar()
prom = est1.promedio(est2)
print("\nPromedio de edad de los estudiantes:", prom)
est1.modificar_edad(22)
print("\nEdad de Estudiante 1 modificada a:", est1.edad)
if est1.misma_edad(doc1):
    print("\nEstudiante 1 tiene la misma edad que el docente.")
if est2.misma_edad(doc1):
    print("Estudiante 2 tiene la misma edad que el docente.")