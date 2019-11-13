class Bola:
    def __init__(self, cor, circ, material):
        self.cor = cor
        self. circ = circ
        self.material = material

    def trocaCor(self):
        self.cor = "Verde"

    def mostraCor(self):
        print(self.cor)


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self):
        self.lado = 5

    def retornarLado(self):
        print(self.lado)

    def calcularArea(self):
        area = self.lado ** 2
        print(area)


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLado(self):
        self.base = 30
        self.altura = 25

    def retornarLado(self):
        print(self.base)
        print(self.altura)

    def calcularArea(self):
        area = self.base * self.altura
        print(area)

    def calcularPerimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print(perimetro)
