class Matriz:
    def __init__(self, identidad=False):
        self.datos = [[0.0 for _ in range(10)] for _ in range(10)]
        if identidad:
            for i in range(10):
                self.datos[i][i] = 1.0
    def sumar(self, otra):
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.datos[i][j] = self.datos[i][j] + otra.datos[i][j]
        return resultado
    def restar(self, otra):
        resultado = Matriz()
        for i in range(10):
            for j in range(10):
                resultado.datos[i][j] = self.datos[i][j] - otra.datos[i][j]
        return resultado
    def igual(self, otra):
        for i in range(10):
            for j in range(10):
                if self.datos[i][j] != otra.datos[i][j]:
                    return False
        return True
    def mostrar(self):
        for fila in self.datos:
            print(fila)
m1 = Matriz(identidad=True)
m2 = Matriz()
m3 = m1.sumar(m2)
m4 = m1.restar(m2)
print("Matriz suma:")
m3.mostrar()
print("Matriz resta:")
m4.mostrar()
print("¿Son iguales m1 y m2?", m1.igual(m2))