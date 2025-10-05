class Celular:
    def __init__(self, nroTel, dueño, espacio, ram, nroApp):
        self.nroTel = nroTel
        self.dueño = dueño
        self.espacio = espacio
        self.ram = ram
        self.nroApp = nroApp
    def instalar_app(self):
        self.nroApp += 10
    def borrar_espacio(self):
        self.espacio -= 5
        if self.espacio < 0:
            self.espacio = 0
    def mostrar(self):
        print(f"Dueño: {self.dueño}")
        print(f"Teléfono: {self.nroTel}")
        print(f"RAM: {self.ram} GB")
        print(f"Espacio: {self.espacio} GB")
        print(f"Nro. Apps: {self.nroApp}")
        print("----------------------------")
cel = Celular("77712345", "Luis", 64, 4, 20)
print("Antes:")
cel.mostrar()
cel.instalar_app()
cel.borrar_espacio()
print("Después:")
cel.mostrar()