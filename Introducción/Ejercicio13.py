class Fruta:
    def __init__(self, nombre, tipo, vitaminas):
        self.nombre = nombre
        self.tipo = tipo
        self.vitaminas = vitaminas
        self.nro_vitaminas = len(vitaminas)
    def mostrar_vitaminas(self):
        print(f"{self.nombre} tiene las vitaminas: {', '.join(self.vitaminas)}")
    def cantidad_citricas(self):
        citricas = ['C']
        return sum(1 for v in self.vitaminas if v in citricas)
    def get_nombre(self):
        return self.nombre
    def get_cantidad_vitaminas(self):
        return self.nro_vitaminas
    def ordenar_vitaminas(self):
        self.vitaminas.sort()
f1 = Fruta("Kiwi", "Subtropical", ["K", "C", "E"])
f2 = Fruta("Naranja", "Cítrica", ["C", "A", "B"])
vitaminas_fresa = ["C", "B", "E"]
f3 = Fruta("Fresa", "Roja", vitaminas_fresa)
f1.mostrar_vitaminas()
f2.mostrar_vitaminas()
f3.mostrar_vitaminas()
frutas = [f1, f2, f3]
mas_vitaminas = max(frutas, key=lambda f: f.get_cantidad_vitaminas())
print("Fruta con más vitaminas:", mas_vitaminas.get_nombre())
print("Vitaminas de la Fresa:")
f3.mostrar_vitaminas()
for f in frutas:
    print(f"{f.get_nombre()} tiene {f.cantidad_citricas()} vitamina(s) cítrica(s)")
for f in frutas:
    f.ordenar_vitaminas()
    print(f"Vitaminas ordenadas de {f.get_nombre()}: {', '.join(f.vitaminas)}")