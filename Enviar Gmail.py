#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message


def enviar_email():  
    corpo_email = """
    <p>Olá Douglas</p>
    <p>Teste de envio de email pela python</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'douglaslespaul@gmail.com'
    msg['To'] = 'douglasllyma@hotmail.com'
    password = 'evlqvfillqslrjfx' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()
