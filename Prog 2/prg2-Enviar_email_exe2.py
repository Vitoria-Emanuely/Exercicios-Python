import urllib.request
import smtplib
import getpass
import requests

# f = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/3496/araquari-sc')
# clima = f.content
# clima = str(clima)
# r = clima.partition(clima.index('<p>'), clima.index('</p>'))
# print(r)
# resultado = r.find('Chuva')

f = urllib.request.urlopen('https://www.cptec.inpe.br/previsao-tempo/sc/joinville').read().decode('utf-8')
f = str(f)
r = f.find('Chuva')

if r != -1:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    senha = getpass.getpass('Digite sua senha')
    smtpObj.login('vikaemanuely@gmail.com', senha)
    smtpObj.sendmail('vikaemanuely@gmail.com', 'vikaemanuely@gmail.com',
                     'Subject:  Aviso: tempo\nOla\n  Vai chover amanha, nao esqueca do guarda-chuva.')
    smtpObj.quit()
else:
    print("Não chove")
