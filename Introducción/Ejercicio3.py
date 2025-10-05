class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}")
        else:
            print("Stock insuficiente.")
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se reabastecieron {cantidad} unidades de {self.nombre}")
    def mostrar(self):
        print(f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}")
p1 = Producto("Pan", 0.5, 100)
p1.vender(20)
p1.reabastecer(50)
p1.mostrar()