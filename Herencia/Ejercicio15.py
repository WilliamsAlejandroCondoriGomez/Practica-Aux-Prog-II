class Nadador:
    def __init__(self, estiloNatacion):
        self.estiloNatacion = estiloNatacion
    def nadar(self):
        print(f"Nadando estilo {self.estiloNatacion}")
class Ciclista:
    def __init__(self, tipoBicicleta):
        self.tipoBicicleta = tipoBicicleta
    def pedalear(self):
        print(f"Pedaleando en bicicleta tipo {self.tipoBicicleta}")
class Corredor:
    def __init__(self, distanciaPreferida):
        self.distanciaPreferida = distanciaPreferida
    def correr(self):
        print(f"Corriendo una distancia de {self.distanciaPreferida} km")
class Triatleta(Nadador, Ciclista, Corredor):
    def __init__(self, estiloNatacion, tipoBicicleta, distanciaPreferida):
        Nadador.__init__(self, estiloNatacion)
        Ciclista.__init__(self, tipoBicicleta)
        Corredor.__init__(self, distanciaPreferida)
triatleta1 = Triatleta("Libre", "Montaña", 10)
triatleta1.nadar()
triatleta1.pedalear()
triatleta1.correr()