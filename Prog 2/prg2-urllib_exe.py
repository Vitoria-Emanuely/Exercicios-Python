import urllib.request

f = urllib.request.urlopen('http://araquari.ifc.edu.br').read().decode('utf-8')
f = str(f)
r = f.find('Sistemas de Informação')

arquivo = open("Resultados.txt", "w+", encoding="UTF-8")

if r != -1:
    arquivo.write("Hoje tem notícia sobre Sistemas de Informação!")
else:
    arquivo.write("Hoje não tem notícia sobre Sistemas de Informação!")
