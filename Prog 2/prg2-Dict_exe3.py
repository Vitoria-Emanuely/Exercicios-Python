'''Leia uma string em português com um texto completo
 e traduza as palavras que encontrar utilizando um dicionário contendo as palavras em
  inglês, retorna o texto completo, com as palavras que encontrou no dicionário traduzidas'''

texto = 'Nenhuma história tem começo e nenhuma história tem fim. Começos e fins podem ser entendidos' \
        ' como algo que serve a um propósito, a uma intenção momentânea e provisória, mas são, em sua natureza fundamental, ' \
        'arbitrários e existem apenas como uma ideia conveniente na mente humana. Todos os começos são arbitrários.'

d = {'nenhuma': 'no', 'história': 'story', 'tem': 'has', 'começo': 'beginning', 'começos': 'beginning', 'e': 'and', 'fim': 'end',
     'fins': 'end', 'podem': 'may', 'entendidos': 'understood', 'como': 'as', 'algo': 'something', 'que': 'that', 'serve': 'serving',
     'uma': 'a', 'intenção': 'intention', 'momentânea': 'momentary', 'provisória': 'provisional', 'mas': 'but', 'são': 'are', 'em': 'in',
     'sua': 'their', 'natureza': 'nature', 'arbitrários': 'arbitrary', 'existem': 'exist', 'fundamental': 'fundamental','apenas': 'only',
     'ideia': 'idea', 'na': 'in', 'mente': 'mind', 'humana': 'human', 'todos': 'all', 'ser': 'be', 'a': 'a', 'um': 'a', 'propósito': 'purpose,',
     'conveniente': 'convinient', 'os': 'the'}


def traduz_para_ingles(texto):
    bad_chars = ['.', ',']
    for i in bad_chars:
        texto = texto.replace(i, '')

    texto = texto.lower().split(' ')
    traducao = [d[w] for w in texto]
    return ' '.join(traducao)

print(traduz_para_ingles(texto))










