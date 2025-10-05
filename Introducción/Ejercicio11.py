class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def mostrar(self):
        print(f"Producto: {self.nombre}, Precio: Bs {self.precio}")
class Pedido:
    def __init__(self):
        self.productos = []
        self.estado = "registrado"
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    def mostrar(self):
        print("Pedido:")
        for p in self.productos:
            p.mostrar()
        print(f"Estado actual: {self.estado}")
p1 = Producto("Café", 10)
p2 = Producto("Croissant", 12)
pedido = Pedido()
pedido.agregar_producto(p1)
pedido.agregar_producto(p2)
pedido.mostrar()
pedido.cambiar_estado("preparado")
pedido.mostrar()
pedido.cambiar_estado("entregado")
pedido.mostrar()