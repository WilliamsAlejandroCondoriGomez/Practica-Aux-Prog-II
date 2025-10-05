class MP4:
    def __init__(self):
        self.canciones = []
        self.videos = []
        self.capacidad_total_kb = 100000
        self.capacidad_usada_kb = 0
    def agregar_cancion(self, nombre, artista, peso_kb):
        for c in self.canciones:
            if c['nombre'] == nombre and c['artista'] == artista:
                print("La canción ya existe.")
                return
        if self.capacidad_usada_kb + peso_kb <= self.capacidad_total_kb:
            self.canciones.append({'nombre': nombre, 'artista': artista, 'peso': peso_kb})
            self.capacidad_usada_kb += peso_kb
        else:
            print("No hay espacio suficiente.")
    def agregar_video(self, nombre, artista, peso_mb):
        peso_kb = peso_mb * 1024
        for v in self.videos:
            if v['nombre'] == nombre and v['artista'] == artista:
                print("El video ya existe.")
                return
        if self.capacidad_usada_kb + peso_kb <= self.capacidad_total_kb:
            self.videos.append({'nombre': nombre, 'artista': artista, 'peso': peso_kb})
            self.capacidad_usada_kb += peso_kb
        else:
            print("No hay espacio suficiente.")
    def borrar_cancion(self, nombre=None, artista=None, peso=None):
        nuevas = []
        for c in self.canciones:
            if (nombre and c['nombre'] != nombre) or \
               (artista and c['artista'] != artista) or \
               (peso and c['peso'] != peso):
                nuevas.append(c)
            else:
                self.capacidad_usada_kb -= c['peso']
        self.canciones = nuevas
    def capacidad_disponible(self):
        return self.capacidad_total_kb - self.capacidad_usada_kb
    def mostrar(self):
        print("Canciones:")
        for c in self.canciones:
            print(f"{c['nombre']} - {c['artista']} ({c['peso']} KB)")
        print("Videos:")
        for v in self.videos:
            print(f"{v['nombre']} - {v['artista']} ({v['peso']//1024} MB)")
        print(f"Espacio disponible: {self.capacidad_disponible()} KB")
mp4 = MP4()
mp4.agregar_cancion("Back To Black", "Amy Winehouse", 100)
mp4.agregar_cancion("Lost On You", "LP", 150)
mp4.agregar_video("Heathens", "twenty one pilots", 50)
mp4.agregar_video("Without Me", "Halsey", 30)
print("\nAntes de borrar:")
mp4.mostrar()
mp4.borrar_cancion(nombre="Back To Black")
print("\nDespués de borrar una canción:")
mp4.mostrar()