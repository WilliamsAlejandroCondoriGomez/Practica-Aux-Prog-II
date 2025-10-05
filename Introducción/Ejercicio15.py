class Carta:
    def __init__(self, codigo, descripcion, remitente, destinatario):
        self.codigo = codigo
        self.descripcion = descripcion
        self.remitente = remitente
        self.destinatario = destinatario
    def contiene_palabra(self, palabra):
        return palabra.lower() in self.descripcion.lower()
    def mostrar(self):
        print(f"Código: {self.codigo}")
        print(f"Remitente: {self.remitente}")
        print(f"Destinatario: {self.destinatario}")
        print(f"Descripción: {self.descripcion}\n")
class Buzon:
    def __init__(self, nro):
        self.nro = nro
        self.cartas = []
    def agregar_carta(self, carta):
        self.cartas.append(carta)
    def eliminar_carta_por_codigo(self, codigo):
        self.cartas = [c for c in self.cartas if c.codigo != codigo]
    def buscar_por_destinatario(self, nombre):
        return [c for c in self.cartas if c.destinatario == nombre]
    def buscar_por_palabra(self, palabra):
        resultados = []
        for c in self.cartas:
            if c.contiene_palabra(palabra):
                resultados.append(c)
        return resultados
c1 = Carta("C123", "Querido amigo, te escribo con amor...", "Juan Alvarez", "Peter Chaves")
c2 = Carta("C456", "Hola Wilmer, espero que ella te ame...", "Pepe Mujica", "Wilmer Pérez")
c3 = Carta("C789", "Querida Paty, te amo mucho", "Paty Vasques", "Pepe Mujica")
b1 = Buzon(1)
b2 = Buzon(2)
b3 = Buzon(3)
b1.agregar_carta(c1)
b1.agregar_carta(c2)
b2.agregar_carta(c3)
b2.agregar_carta(c1)
b3.agregar_carta(c2)
cartas_wilmer = b1.buscar_por_destinatario("Wilmer Pérez")
print("Cartas para Wilmer Pérez:")
for c in cartas_wilmer:
    c.mostrar()
b1.eliminar_carta_por_codigo("C456")
print("Cartas que contienen la palabra 'amor':")
for buz in [b1, b2, b3]:
    for carta in buz.buscar_por_palabra("amor"):
        carta.mostrar()