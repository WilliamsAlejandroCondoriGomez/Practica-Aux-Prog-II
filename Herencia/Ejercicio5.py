class Vehiculo:
    def __init__(self, id, placa, conductor):
        self._id = id
        self._placa = placa
        self._conductor = conductor
    def mostrar_datos(self):
        print("Placa:", self._placa)
        print("Conductor:", self._conductor)
    def cambiar_conductor(self, nuevo_conductor):
        self._conductor = nuevo_conductor
class Bus(Vehiculo):
    def __init__(self, id, placa, conductor, capacidad, sindicato):
        super().__init__(id, placa, conductor)
        self.capacidad = capacidad
        self.sindicato = sindicato
class Auto(Vehiculo):
    def __init__(self, id, placa, conductor, caballosFuerza, descapotable):
        super().__init__(id, placa, conductor)
        self.caballosFuerza = caballosFuerza
        self.descapotable = descapotable
class Moto(Vehiculo):
    def __init__(self, id, placa, conductor, cilindrada, casco):
        super().__init__(id, placa, conductor)
        self.cilindrada = cilindrada
        self.casco = casco
bus = Bus(1, "123-ABC", "Carlos", 50, "Sindicato A")
auto = Auto(2, "456-DEF", "Ana", 120, True)
moto = Moto(3, "789-GHI", "Luis", 250, True)
print("BUS:")
bus.mostrar_datos()
print("\nAUTO:")
auto.mostrar_datos()
print("\nMOTO:")
moto.mostrar_datos()
print("\nCAMBIO DE CONDUCTOR DEL AUTO:")
auto.cambiar_conductor("Pedro")
auto.mostrar_datos()