class Videojuego:
    def __init__(self, nombre="SinNombre", plataforma="Desconocida", cantidad_jugadores=0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cantidad_jugadores = cantidad_jugadores
    def agregar_jugadores(self, cantidad=1):
        self.cantidad_jugadores += cantidad
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Plataforma: {self.plataforma}, Jugadores: {self.cantidad_jugadores}")
v1 = Videojuego("FIFA 25", "PlayStation", 2)
v2 = Videojuego()
v1.agregar_jugadores()
v2.agregar_jugadores(3)
v1.mostrar()
v2.mostrar()