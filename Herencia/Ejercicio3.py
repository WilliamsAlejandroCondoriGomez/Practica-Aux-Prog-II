class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def desplazarse(self):
        print(f"{self.nombre} se desplaza de alguna forma.")
class Leon(Animal):
    def desplazarse(self):
        print(f"{self.nombre} camina con fuerza.")
class Pinguino(Animal):
    def desplazarse(self):
        print(f"{self.nombre} nada ágilmente.")
class Canguro(Animal):
    def desplazarse(self):
        print(f"{self.nombre} salta grandes distancias.")
animales = [
    Leon("Simba", 5),
    Pinguino("Pingu", 3),
    Canguro("Jack", 4)
]
for a in animales:
    a.desplazarse()