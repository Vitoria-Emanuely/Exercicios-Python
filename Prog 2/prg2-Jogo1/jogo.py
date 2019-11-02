import random
arquivo = open('lista.txt').read().splitlines()
palavra = random.choice(arquivo)
embaralha = "".join(random.sample(palavra, len(palavra)))
tentativa = 5
n_tentativa = 1
print("Seja bem-vindo(a) ao Jogo 1.0! \n")
print(embaralha)
pergunta = input(str("Qual é a palavra correta? "))
posicao = 1

animo = {1: "Você errou, tente novamente :D \n",
         2: "Não desista, só os fortes continuam!!! \n",
         3: "Só com a persistência você alcança seus objetivos! \n",
         4: "Eu acredito em você, tente mais uma vez vencedor! \n",
         5: "Errar é uma humano, persistir no erro é burrice! \n"}

while pergunta != palavra and tentativa != 1:
    tentativa -= 1
    n_tentativa += 1
    print(animo[posicao])
    posicao += 1
    print("Você tem %d tentativa(s)" % tentativa)
    pergunta = input(str("Qual é a palavra correta? "))

if pergunta != palavra:
    print(animo[posicao])
    print("A palavra correta era: %s \n" % palavra)
else:
    print("Parabéns você acertou!")
print("Você utilizou %d tentativa(s)" % n_tentativa)
print("Fim de jogo :D")