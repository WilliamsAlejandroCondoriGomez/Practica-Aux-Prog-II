class Politico:
    def __init__(self, profesion, años_exp):
        self.profesion = profesion
        self.años_exp = años_exp
class Partido:
    def __init__(self, nombre_p, rol):
        self.nombre_p = nombre_p
        self.rol = rol
class Presidente(Politico, Partido):
    def __init__(self, nombre, apellido, profesion, años_exp, nombre_p, rol):
        Politico.__init__(self, profesion, años_exp)
        Partido.__init__(self, nombre_p, rol)
        self.nombre = nombre
        self.apellido = apellido
    def mostrar_info(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Profesión:", self.profesion)
        print("Años de experiencia:", self.años_exp)
        print("Partido político:", self.nombre_p)
        print("Rol en el partido:", self.rol)
pres1 = Presidente("Luis", "Arce", "Economista", 25, "MAS", "Presidente del partido")
nombre = "Carlos"
apellido = "Mesa"
profesion = "Historiador"
años_exp = 20
nombre_p = "CC"
rol = "Candidato"
pres2 = Presidente(nombre, apellido, profesion, años_exp, nombre_p, rol)
print("Presidente 1:")
pres1.mostrar_info()
print("\nPresidente 2:")
pres2.mostrar_info()
presidentes = [
    pres1,
    pres2,
    Presidente("Evo", "Morales", "Sindicalista", 30, "MAS", "Fundador")
]
nombre_buscado = "Evo"
encontrado = False
for p in presidentes:
    if p.nombre == nombre_buscado:
        print("\nPresidente encontrado:")
        print("Nombre:", p.nombre)
        print("Partido político:", p.nombre_p)
        print("Profesión:", p.profesion)
        encontrado = True
if not encontrado:
    print("\nNo se encontró al presidente con nombre", nombre_buscado)