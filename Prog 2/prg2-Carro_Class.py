class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.qtd_combustivel = 0

    def andar(self, km):
        gasto = km / self.consumo
        self.qtd_combustivel -= gasto

    def obterGasolina(self):
        print(round(self.qtd_combustivel, 2))

    def adicionarGasolina(self, litros):
        self.qtd_combustivel += litros


fox = Carro(15)
fox.adicionarGasolina(20)
fox.andar(100)
fox.obterGasolina()
