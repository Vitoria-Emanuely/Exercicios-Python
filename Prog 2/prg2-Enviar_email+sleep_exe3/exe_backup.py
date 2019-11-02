import datetime
import time
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib

def enviarEmail():
    sender_email = "joaosilvapires3@gmail.com"
    receiver_email = "joaosilvapires3@gmail.com"
    password = "SenhaGmail_5@"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Backup efetuado com sucesso"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Oĺá,
    Seu backup foi efetuado com sucesso!"""
    html = """\
    <html>
      <body>
        <p>Olá,<br>
           Seu backup foi efetuado com sucesso!<br>
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def verificarEmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('joaosilvapires3@gmail.com', 'SenhaGmail_5@')
    mail.list()
    mail.select("inbox")
    resultado = mail.uid('search', None, '(HEADER Subject "Backup efetuado com sucesso")')
    return resultado


enviado = False

while enviado is False:
    arquivo = open('arquivo.txt', encoding='UTF-8').read().splitlines()
    for linha in arquivo:
        if linha == "backup efetuado com sucesso":
            enviarEmail()
            atual = datetime.date.today()
            amanha = datetime.date.today() + datetime.timedelta(days=1)
            while verificarEmail():
                if amanha >= atual:
                    break
    time.sleep(300)

