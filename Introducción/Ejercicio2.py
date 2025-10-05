class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
        else:
            print("No hay suficientes asientos disponibles.")
    def cobrar_pasajes(self):
        return self.pasajeros * 1.5
    def asientos_disponibles(self):
        return self.capacidad - self.pasajeros
bus1 = Bus(40)
bus1.subir_pasajeros(25)
print("Pasaje cobrado:", bus1.cobrar_pasajes())
print("Asientos disponibles:", bus1.asientos_disponibles())