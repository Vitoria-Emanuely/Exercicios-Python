cab = input('Digite o cabeçalho da página:')
tituloPag = input('Digite o título da página:')

arquivo = open('ola.html', 'w', encoding='utf-8')

arquivo.write('''
<html>
    <title>{}</title>
    <body> 
        <h1>{}</h1>
'''.format(cab, tituloPag))

post = 1
while post < 3:

    tituloTexto = input("Digite o título do texto:").format(post)
    link = input("Digite o link da postagem:")
    descricao = input("Digite a descrição da postagem:")

    arquivo.write('''
        <div>
              <a href=" {} "><h3> {} </h3></a>
              <p> {} </p>
        </div>
    </body>
</html>
    
    
    '''.format(link, tituloTexto, descricao))
    post += 1

arquivo.close()