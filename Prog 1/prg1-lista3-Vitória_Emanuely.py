#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 5

def palindrome(texto):
    '''Faça uma função que verifique se um texto passado é palíndrome,
    isto é, se é igual quando lido de trás pra frente.'''
    texto = texto.lower().strip(' ')
    novo_texto = ''
    for letra in texto:
        if letra.isalpha():
            novo_texto += letra
    texto = novo_texto
    novo = texto[::-1]
    if texto == novo:
        return True
    else:
        return False

def troca_caixa(texto):
    '''Vogais ficam em caixa alta (maiúsculas)
    Consoantes ficam em caixa baixa (minúsculas)'''
    novo = ''
    for letra in texto:
        if letra in 'aeiouAEIOU':
            novo += letra.upper()
        else:
            novo += letra.lower()
    return novo

def imprime_mes_por_extenso(data):
    '''Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
    e imprima com o nome do mês por extenso
    '''
    meses = 'janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split()
    dia, mes, ano = data.split('/')
    mes_extenso = meses[int(mes) - 1]
    data_extenso = '%s de %s de %s' % (dia, mes_extenso, ano)
    return data_extenso

def encontra_caracter(texto, caracter_procurado):
    '''Receba um texto e retorne a localização da primeira vez que
    aparece o caracter especificado. Não use texto.find().'''
    posicao = 0
    for letra in texto:
        if letra == caracter_procurado:
            return posicao
        posicao += 1
    return -1

def é_sortudo(numero):
    '''um número é sortudo se ele contém o dígito 2 mas não o dígito 7.'''
    numero = str(numero)
    if '2' in numero and '7' not in numero:
        return True
    else:
        return False

def numeros_sortudos(limite_inferior=1, limite_superior=100000):
    ''' Daniela é uma pessoa muito supersticiosa. Para ela, um número é
    sortudo se ele contém o dígito 2 mas não o dígito 7.
    Faça então uma função que informe a ela quantos números sortudos
    existem entre um intervalo dado, incluindo os extremos.
    Por exemplo: entre 18644 e 33087, existem 7995 números sortudos.
    Dica: faça uma função de validação e outra que a chama e
    verifica o intervalo dado
    '''
    sortudo = 0
    while limite_inferior <= limite_superior:
        if é_sortudo(limite_inferior) is True:
            sortudo += 1
        limite_inferior += 1
    return sortudo

def é_azarado(numero):
    '''O último dígito não pode ser igual ao primeiro, porque isso dá azar
    '''
    ultimo = numero[::-1]
    if numero[0] == ultimo[0]:
        return True
    else:
        return False

def soma_é_par(numero):
    '''A soma dos dígitos tem que ser par, porque isso é legal;
    '''
    soma = 0
    for digito in numero:
        soma += int(digito)
    if soma % 2 == 0:
        return True
    else:
        return False

def é_chato(numero):
    '''Não pode haver dois dígitos consecutivos idênticos, porque isso é chato.'''
    anterior = ''
    for atual in numero:
        if atual == anterior:
            return True
        anterior = atual
    return False

def é_número_válido(numero):
    '''Um número é válido se não é azarado, a soma é par e não é chato.'''
    if é_azarado(numero) and soma_é_par(numero) and é_chato(numero) is True:
        return True
    else:
        return False

def ponteironuloville(telefones):
    '''Na pacata vila campestre de Ponteironuloville, todos os telefones
    têm 6 dígitos. A companhia telefônica estabelece as seguintes regras
    sobre os números:
    1. Não pode haver dois dígitos consecutivos idênticos, porque isso é chato;

    2. A soma dos dígitos tem que ser par, porque isso é legal;
    3. O último dígito não pode ser igual ao primeiro, porque isso dá azar.

    Então, dadas essas regras perfeitamente razoáveis, bem projetadas e
    maduras, quantos números de telefone na lista abaixo são válidos?
    Dica: faça uma função de validação e outra que a chama e verifica os
    valores passados.
    Outra dica: coloque a lista em um arquivo texto
    Mais uma dica: você precisa incluir um teste com esses valores.

        213752 216732 221063 221545 225583 229133 230648 233222
        236043 237330 239636 240138 242123 246224 249183 252936
        254711 257200 257607 261424 263814 266794 268649 273050
        275001 277606 278997 283331 287104 287953 289137 291591
        292559 292946 295180 295566 297529 300400 304707 306931
        310638 313595 318449 319021 322082 323796 326266 326880
        327249 329914 334392 334575 336723 336734 338808 343269
        346040 350113 353631 357154 361633 361891 364889 365746
        365749 366426 369156 369444 369689 372896 374983 375223
        379163 380712 385640 386777 388599 389450 390178 392943
        394742 395921 398644 398832 401149 402219 405364 408088
        412901 417683 440052 444630 463328 466458 486195 488359
        500877 502386 521455 524277 536593 537360 556493 558807
        579937 580112 590483 593112 601523 605761 618314 622752
        637656 641136 662224 666265 422267 447852 469601 489209
        502715 528496 539055 559102 580680 593894 608618 626345
        644176 668010 424767 449116 473108 489388 507617 529345
        540582 562050 582458 594293 609198 626632 644973 672480
        426613 453865 476773 491928 512526 531231 543708 564962
        583012 597525 610141 628889 647617 672695 430474 457631
        477956 496569 512827 531766 547492 569677 585395 598184
        610536 629457 652218 676868 433910 461750 481991 496964
        513796 535067 550779 570945 586244 600455 612636 629643
        657143 677125 435054 462985 482422 497901 518232 535183
        551595 575447 587393 600953 615233 633673 659902 678315

        Resposta: 39
    '''
    x = 0
    for telefone in telefones:
        if not é_azarado(telefone) and soma_é_par(telefone) and not é_chato(telefone):
            x += 1
    return x

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print(' Palindrome:')
    test(palindrome("ovo"), True)  # normal
    test(palindrome("Ovo"), True)  # mudança de caixa
    test(palindrome("Ovo "), True)  # espaço no final
    test(palindrome(" Ovo "), True)  # espaço no início
    test(palindrome('Assam a massa'), True)  # frases (espaços em branco)
    test(palindrome('Ame o poema!'), True)  # frases com pontuação
    test(palindrome('1-Bom dia, Araquari, sua "linda"!'), False)  # frases com pontuação

    print(' Troca caixa:')
    test(troca_caixa("Araquari"), "ArAqUArI")  # normal
    test(troca_caixa("Caxias do Sul"), "cAxIAs dO sUl")  # com espaços

    print(' Mês por extenso:')
    test(imprime_mes_por_extenso("01/01/2017"), "01 de janeiro de 2017")
    test(imprime_mes_por_extenso("19/05/2014"), "19 de maio de 2014")
    test(imprime_mes_por_extenso("25/12/2016"), "25 de dezembro de 2016")

    print(' Encontra caracter:')
    test(encontra_caracter("--*--", "*"), 2)
    test(encontra_caracter("19/05/2014", "/"), 2)
    test(encontra_caracter("19/05/2014", "."), -1)

    print(' É sortudo:')
    test(é_sortudo(2), True)
    test(é_sortudo(7), False)
    test(é_sortudo(27), False)
    test(é_sortudo(72), False)
    test(é_sortudo(35), False)
    test(é_sortudo(37), False)
    test(é_sortudo(21), True)

    print(' Números sortudos:')
    test(numeros_sortudos(10, 20), 2)
    test(numeros_sortudos(18644, 33087), 7995)

    print(' É azarado:')
    test(é_azarado('213452'), True)
    test(é_azarado('213451'), False)
    test(é_azarado('123456'), False)

    print(' A soma é par:')
    test(soma_é_par('222222'), True)
    test(soma_é_par('222221'), False)
    test(soma_é_par('123456'), False)

    print(' É chato:')
    test(é_chato('123455'), True)
    test(é_chato('123445'), True)
    test(é_chato('223456'), True)
    test(é_chato('122345'), True)
    test(é_chato('123456'), False)

    print(' É número válido:')
    test(é_número_válido('123456'), False)
    test(é_número_válido('113456'), False)
    test(é_número_válido('213452'), False)

    print(' Ponteironuloville:')
    telefones = ['91775523', '88032828']
    test(ponteironuloville(telefones), 0)
    telefones = '''
        213752 216732 221063 221545 225583 229133 230648 233222
        236043 237330 239636 240138 242123 246224 249183 252936
        254711 257200 257607 261424 263814 266794 268649 273050
        275001 277606 278997 283331 287104 287953 289137 291591
        292559 292946 295180 295566 297529 300400 304707 306931
        310638 313595 318449 319021 322082 323796 326266 326880
        327249 329914 334392 334575 336723 336734 338808 343269
        346040 350113 353631 357154 361633 361891 364889 365746
        365749 366426 369156 369444 369689 372896 374983 375223
        379163 380712 385640 386777 388599 389450 390178 392943
        394742 395921 398644 398832 401149 402219 405364 408088
        412901 417683 440052 444630 463328 466458 486195 488359
        500877 502386 521455 524277 536593 537360 556493 558807
        579937 580112 590483 593112 601523 605761 618314 622752
        637656 641136 662224 666265 422267 447852 469601 489209
        502715 528496 539055 559102 580680 593894 608618 626345
        644176 668010 424767 449116 473108 489388 507617 529345
        540582 562050 582458 594293 609198 626632 644973 672480
        426613 453865 476773 491928 512526 531231 543708 564962
        583012 597525 610141 628889 647617 672695 430474 457631
        477956 496569 512827 531766 547492 569677 585395 598184
        610536 629457 652218 676868 433910 461750 481991 496964
        513796 535067 550779 570945 586244 600455 612636 629643
        657143 677125 435054 462985 482422 497901 518232 535183
        551595 575447 587393 600953 615233 633673 659902 678315
    '''.strip().split()
    test(ponteironuloville(telefones), 39)
    telefones = open('telefones.txt').read().strip().split()
    test(ponteironuloville(telefones), 39)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")