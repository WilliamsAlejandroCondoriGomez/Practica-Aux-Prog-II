class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Empleado:
    def __init__(self, id_empleado, sueldo):
        self.id_empleado = id_empleado
        self.sueldo = sueldo
class Policia:
    def __init__(self, grado, unidad):
        self.grado = grado
        self.unidad = unidad
class JefePolicia(Persona, Empleado, Policia):
    def __init__(self, nombre, edad, id_empleado, sueldo, grado, unidad):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, id_empleado, sueldo)
        Policia.__init__(self, grado, unidad)
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("ID Empleado:", self.id_empleado)
        print("Sueldo:", self.sueldo)
        print("Grado:", self.grado)
        print("Unidad:", self.unidad)
    def comparar_sueldo(self, otro):
        if self.sueldo > otro.sueldo:
            print(self.nombre, "tiene mayor sueldo que", otro.nombre)
        elif self.sueldo < otro.sueldo:
            print(otro.nombre, "tiene mayor sueldo que", self.nombre)
        else:
            print("Ambos tienen el mismo sueldo")
    def mismo_grado(self, otro):
        return self.grado == otro.grado
jefe1 = JefePolicia("Carlos", 45, "EMP001", 5000.0, "Capitán", "Antinarcóticos")
jefe2 = JefePolicia("Luis", 50, "EMP002", 5500.0, "Capitán", "Investigación")
print("Datos del Jefe 1:")
jefe1.mostrar_datos()
print("\nDatos del Jefe 2:")
jefe2.mostrar_datos()
print("\nComparación de sueldos:")
jefe1.comparar_sueldo(jefe2)
print("\n¿Tienen el mismo grado?")
if jefe1.mismo_grado(jefe2):
    print("Sí, ambos tienen el mismo grado:", jefe1.grado)
else:
    print("No, tienen grados diferentes.")