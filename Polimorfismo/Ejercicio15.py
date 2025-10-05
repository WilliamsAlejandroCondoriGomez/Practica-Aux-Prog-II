class Ordenador:
    def __init__(self, serial, numero, ram, procesador, estado):
        self.serial = serial
        self.numero = numero
        self.ram = ram
        self.procesador = procesador
        self.estado = estado
    def mostrar(self):
        print(f"Serial: {self.serial}, Nº: {self.numero}, RAM: {self.ram} GB, Proc: {self.procesador}, Estado: {self.estado}")
class Laboratorio:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ordenadores = []
    def agregar_ordenador(self, ordenador):
        if len(self.ordenadores) < self.capacidad:
            self.ordenadores.append(ordenador)
        else:
            print("Capacidad llena.")
    def informacion_por_estado(self, estado):
        print(f"--- {self.nombre} | Estado: {estado} ---")
        for o in self.ordenadores:
            if o.estado == estado:
                o.mostrar()
    def informacion_por_ram(self, min_ram):
        print(f"--- {self.nombre} | RAM > {min_ram} ---")
        for o in self.ordenadores:
            if o.ram > min_ram:
                o.mostrar()
    def mostrar_todos(self):
        print(f"=== Laboratorio: {self.nombre} ===")
        for o in self.ordenadores:
            o.mostrar()
    def trasladar_a(self, destino, cantidad):
        trasladados = self.ordenadores[:cantidad]
        self.ordenadores = self.ordenadores[cantidad:]
        for o in trasladados:
            destino.agregar_ordenador(o)
        print(f"Se trasladaron {len(trasladados)} ordenadores de {self.nombre} a {destino.nombre}.")
o1 = Ordenador("A1", 1, 4, "Intel", "activo")
o2 = Ordenador("B2", 2, 16, "AMD", "inactivo")
o3 = Ordenador("C3", 3, 8, "Intel", "activo")
o4 = Ordenador("D4", 4, 12, "Intel", "activo")
o5 = Ordenador("E5", 5, 6, "AMD", "inactivo")
o6 = Ordenador("F6", 6, 10, "Intel", "activo")
lab1 = Laboratorio("Lasin 1", 10)
lab2 = Laboratorio("Lasin 2", 10)
for o in [o1, o2, o3, o4, o5, o6]:
    lab1.agregar_ordenador(o)
print("\nAntes del traslado:")
lab1.mostrar_todos()
lab2.mostrar_todos()
lab1.trasladar_a(lab2, 2)
print("\nDespués del traslado:")
lab1.mostrar_todos()
lab2.mostrar_todos()
lab1.informacion_por_estado("activo")
lab2.informacion_por_ram(8)