import os 
import smtplib
from email.message import EmailMessage
from segredo import senha 

# Configuração de email e senha 
EMAIL_ADDRES = 'douglaslespaul@gmail.com'
# Crie um arquivo para armazenar a senha 
# nesse caso crie um arquivo python chamdo segredo 
# contendo uma variavel 'senha' e importei aqui.
EMAIL_PASSWORD = senha 

# Criar Email
msg = EmailMessage()
msg['Subject'] = 'Email de Teste'
msg['From'] = 'douglaslespaul@gmail.com'
msg['To'] = 'douglasllyma@hotmail.com, douglaslespaul@gmail.com'
msg.set_content('Teste de Programa para envio de emails')


# Enviar um e-mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRES, EMAIL_PASSWORD)
        smtp.send_message(msg)
print('Email enviado com sucesso!')


