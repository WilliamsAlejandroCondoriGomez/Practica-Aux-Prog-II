class Empleado:
    def __init__(self, nombre: str, sueldomes: float):
        self.nombre = nombre
        self.sueldomes = sueldomes
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Sueldo Mensual: {self.sueldomes}")
    def sueldo_total(self):
        return self.sueldomes
class Administrativo(Empleado):
    def __init__(self, nombre: str, sueldomes: float, cargo: str):
        super().__init__(nombre, sueldomes)
        self.cargo = cargo
    def mostrar(self):
        super().mostrar()
        print(f"Cargo: {self.cargo}")
    def sueldo_total(self):
        return super().sueldo_total()
class Chef(Empleado):
    def __init__(self, nombre: str, sueldomes: float, horaExtra: int, tipo: str, sueldoHora: float):
        super().__init__(nombre, sueldomes)
        self.horaExtra = horaExtra
        self.tipo = tipo
        self.sueldoHora = sueldoHora
    def mostrar(self):
        super().mostrar()
        print(f"Tipo: {self.tipo}")
        print(f"Horas Extra: {self.horaExtra}")
        print(f"Sueldo por Hora: {self.sueldoHora}")
    def sueldo_total(self):
        return self.sueldomes + (self.horaExtra * self.sueldoHora)
class Mesero(Empleado):
    def __init__(self, nombre: str, sueldomes: float, propina: float, horaExtra: int, sueldoHora: float):
        super().__init__(nombre, sueldomes)
        self.propina = propina
        self.horaExtra = horaExtra
        self.sueldoHora = sueldoHora
    def mostrar(self):
        super().mostrar()
        print(f"Propina: {self.propina}")
        print(f"Horas Extra: {self.horaExtra}")
        print(f"Sueldo por Hora: {self.sueldoHora}")
    def sueldo_total(self):
        return self.sueldomes + (self.horaExtra * self.sueldoHora) + self.propina
chef1 = Chef("Luis", 2000.0, 10, "Principal", 50.0)
mesero1 = Mesero("Ana", 1200.0, 200.0, 5, 20.0)
mesero2 = Mesero("Juan", 1200.0, 150.0, 3, 25.0)
admin1 = Administrativo("Carla", 1800.0, "Contadora")
admin2 = Administrativo("Mario", 1800.0, "Gerente")
empleados = [chef1, mesero1, mesero2, admin1, admin2]
print("\nEmpleados con sueldo mensual igual a 1800.0:")
for emp in empleados:
    if emp.sueldomes == 1800.0:
        emp.mostrar()
        print("-----------")
print("\nSueldo total de todos los empleados:")
for emp in empleados:
    print(f"{emp.nombre} - Sueldo Total: {emp.sueldo_total()}")