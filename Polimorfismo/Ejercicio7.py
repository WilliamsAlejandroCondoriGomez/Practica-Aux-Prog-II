class Sistema:
    def __init__(self, admins=None, autos=None):
        if admins is None:
            self.admins = []
        else:
            self.admins = admins
        if autos is None:
            self.autos = []
        else:
            self.autos = autos
    def adicionar_admin(self, admin):
        self.admins.append(admin)
    def adicionar_auto(self, modelo, placa, color):
        self.autos.append([modelo, placa, color])
    def mostrar(self):
        print("=== Administradores ===")
        for a in self.admins:
            print(f"- {a}")
        print("=== Autos ===")
        for auto in self.autos:
            print(f"Modelo: {auto[0]}, Placa: {auto[1]}, Color: {auto[2]}")
        print("------------------------")
sistema1 = Sistema()
sistema1.adicionar_admin("Carlos")
sistema1.adicionar_auto("Toyota", "123-ABC", "Rojo")
sistema2 = Sistema(["Laura"], [["Nissan", "456-DEF", "Negro"]])
sistema1.mostrar()
sistema2.mostrar()