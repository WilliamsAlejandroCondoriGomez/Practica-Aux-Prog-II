class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100
    def alimentar(self):
        self.energia += 20
        if self.energia > 100:
            self.energia = 100
        print(f"{self.nombre} ha sido alimentado. Energía: {self.energia}")
    def jugar(self):
        self.energia -= 15
        if self.energia < 0:
            self.energia = 0
        print(f"{self.nombre} ha jugado. Energía: {self.energia}")
    def mostrar_energia(self):
        print(f"{self.nombre} tiene {self.energia} de energía.")
m1 = Mascota("Firulais")
m2 = Mascota("Pelusa")
m1.alimentar()
m1.jugar()
m1.mostrar_energia()
m2.jugar()
m2.alimentar()
m2.mostrar_energia()