class Pasajero:
    def __init__(self, nombre, habitacion, costo, genero):
        self.nombre = nombre
        self.habitacion = habitacion
        self.costo_pasaje = costo
        self.genero = genero
    def mostrar(self):
        print(f"{self.nombre} - Habitación: {self.habitacion} - Costo: {self.costo_pasaje} - Género: {self.genero}")
class Crucero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pasajeros = []
    def agregar_pasajero(self, p):
        self.pasajeros.append(p)
    def mostrar_pasajeros(self):
        print(f"--- Crucero: {self.nombre} ---")
        for p in self.pasajeros:
            p.mostrar()
    def total_pasajes(self):
        return sum(p.costo_pasaje for p in self.pasajeros)
    def comparar_pasajeros(self, otro):
        return len(self.pasajeros) == len(otro.pasajeros)
    def contar_generos(self):
        hombres = sum(1 for p in self.pasajeros if p.genero == "M")
        mujeres = sum(1 for p in self.pasajeros if p.genero == "F")
        return hombres, mujeres
c1 = Crucero("Titanic")
c2 = Crucero("Olympic")
p1 = Pasajero("Juan Vargas", 502, 500, "M")
p2 = Pasajero("Martina Vasques", 603, 1000, "F")
p3 = Pasajero("Wilmer Montero", 401, 925, "M")
p4 = Pasajero("Lina Perez", 101, 800, "F")
p5 = Pasajero("Carlos Gomez", 202, 950, "M")
c1.agregar_pasajero(p1)
c1.agregar_pasajero(p2)
c2.agregar_pasajero(p3)
c2.agregar_pasajero(p4)
c2.agregar_pasajero(p5)
c1.mostrar_pasajeros()
c2.mostrar_pasajeros()
print("Total pasajes C1:", c1.total_pasajes())
print("Total pasajes C2:", c2.total_pasajes())
print("¿Misma cantidad de pasajeros?", c1.comparar_pasajeros(c2))
h, m = c2.contar_generos()
print("Hombres:", h, "Mujeres:", m)