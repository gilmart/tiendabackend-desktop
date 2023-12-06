class Heroe:

    def __init__(self, nombreAsignado, colorAsignado, poderAsignado):
        self.nombre=nombreAsignado
        self.color=colorAsignado
        self.poder=poderAsignado

    def saludar(self):
        print(f'hola, soy {self.nombre}')
