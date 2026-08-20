from personaje import Personaje

class Mago(Personaje):

    def __init__(self, nombre, nivel, vida, poder__magico):
        super().__init__(nombre, nivel, vida)
        self.poder_magico = poder__magico

    def atacar(self):
        print(f"{self.nombre} lanza un hechizo "
              f"con {self.poder_magico} de poder magico")