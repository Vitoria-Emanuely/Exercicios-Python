import random


def escolha_nivel():
    nivelPessoa = 1
    while 0 < nivelPessoa < 4:
        nivelPessoa = input("Escolha um nível: \n 1. Fácil \n 2. Médio \n 3. Difícil \n")
        nivelPessoa = int(nivelPessoa)
        if nivelPessoa == 1:
            return facil()
        elif nivelPessoa == 2:
            return medio()
        elif nivelPessoa == 3:
            return dificil()
        else:
            print('Você digitou um nível que não existe, tente novamente!')
    print("Escolha um nível entre 1 e 3")
    return escolha_nivel()


def facil():
    arquivo = open('facil.txt').read().splitlines()
    return escolher_palavra(arquivo)


def medio():
    arquivo = open('medio.txt').read().splitlines()
    return escolher_palavra(arquivo)


def dificil():
    arquivo = open('dificil.txt').read().splitlines()
    return escolher_palavra(arquivo)


def escolher_palavra(arquivo):
    palavra = random.choice(arquivo)
    embaralha = "".join(random.sample(palavra, len(palavra)))
    return tentativas(embaralha, palavra)


def animo():
    arquivo = open('animo.txt').read().splitlines()
    palavra = random.choice(arquivo)
    print(palavra)


def tentativas(embaralha, palavra):
    tentativa = 5
    n_tentativa = 0
    print(embaralha)
    while tentativa != 0:
        pergunta = input(str("Qual é a palavra correta? "))
        n_tentativa += 1
        tentativa = rodada(palavra, pergunta, tentativa, n_tentativa)
    print("A palavra correta era: %s" % palavra)
    print("Fim de Jogo :D")


def rodada(palavra, pergunta, tentativa, n_tentativa):
    if pergunta != palavra:
        animo()
        tentativa -= 1

        print("Você tem mais %d tentativa(s) \n" % tentativa)
    else:
        print("Parabéns, você acertou!!! \n")
        print("Você utilizou %d tentativa(s) \n" % n_tentativa)
        tentativa = 0
    return tentativa


#Interação
print("Seja bem-vindo(a) ao Jogo 2.0 \n")
escolha_nivel()

