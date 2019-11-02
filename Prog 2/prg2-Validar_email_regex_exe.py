import re


def validaEmail(email):
    validacao = re.search(r'[\w]+@\w+(.com[.br]*)+', email)
    if validacao:
        return True
    else:
        return False


def checagem():
    email = input("Digite o seu email: ")
    validaEmail(email)
    if validaEmail(email):
        print("Email válido")
    else:
        print("Email inválido")
        checagem()


checagem()
