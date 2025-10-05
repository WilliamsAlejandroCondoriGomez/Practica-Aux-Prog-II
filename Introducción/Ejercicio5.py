class Persona:
    def __init__(self, nombre, paterno, materno, edad, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci
    def mostrar_datos(self):
        print(f"Nombre completo: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad} - CI: {self.ci}")
    def mayor_de_edad(self):
        return self.edad >= 18
    def modificar_edad(self, nuevo):
        self.edad = nuevo
    def mismo_apellido(self, otra_persona):
        return self.paterno == otra_persona.paterno
p1 = Persona("Ana", "Lopez", "Perez", 20, "1234567")
p2 = Persona("Juan", "Lopez", "Sosa", 17, "7654321")
p1.mostrar_datos()
print("¿Mayor de edad?", p1.mayor_de_edad())
p2.modificar_edad(18)
print("¿Mismo apellido paterno?", p1.mismo_apellido(p2))