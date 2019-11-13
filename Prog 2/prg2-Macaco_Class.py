class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        for item in self.bucho:
            print(str(item))

    def digerir(self):
        self.bucho = []
        print("Estou com fome!!!! \n")


macaco1 = Macaco("Alfredo")
macaco2 = Macaco("Rodolfo")

print("Dados Macaco 1")
macaco1.comer("batata")
macaco1.verBucho()
macaco1.comer("rucula")
macaco1.verBucho()
macaco1.comer("alface")
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()

print("Dados Macaco 2")
macaco2.comer("chocolate")
macaco2.verBucho()
macaco2.comer("batata frita")
macaco2.verBucho()
macaco2.comer("empadão")
macaco2.verBucho()
macaco2.digerir()
macaco2.verBucho()

print("Macaco virando canibal")
macaco1.comer(macaco2)
macaco1.verBucho()
