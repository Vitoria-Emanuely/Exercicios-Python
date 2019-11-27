import os


def inicio():
    print("\nPara administrar o sistema escolha uma das opções abaixo: \n")
    print("Opção 1: Visualizar informações do sistema")
    print("Opção 2: Visualizar uso de disco")
    print("Opção 3: Fazer ping")
    print("Opção 4: Sair do sistema")
    return input("Digite o que deseja fazer: ")


def opcao1():
    return os.system("uname -a")


def opcao2():
    return os.system("df -h")


def opcao3():
    host = input(str("Digite o IP que deseja pingar: "))
    count = input(str("Digite quantos pings deseja fazer: "))
    return os.system("ping %s -c %s" % (host, count))


def opcao4():
    exit()
    return os.system("exit")


def opcoes():
    if resposta == "1":
        opcao1()
    elif resposta == "2":
        opcao2()
    elif resposta == "3":
        opcao3()
    elif resposta == "4":
        opcao4()
    else:
        print("\nDigite uma opção válida")


resposta = inicio()
opcoes()


while resposta:
    resposta = inicio()
    opcoes()
