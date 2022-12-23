# Escreva um programa que faça o computador pensar em um 
# número inteiro entre 0 e 5 e peça para o usuário 
# tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário 
# venceu ou perdeu.
from random import randint
from time import sleep


num = randint(0,5)
print('<->'*20)
num1 = int(input('Digite um número de 0 a 5: '))
print('<->'*20)
print('PROCESSANDO->->->->')
sleep(3)


if num == num1:
    print('Parabéns>>>Acertou!') 
else:
    print(f'Errou...O número correto é {num}!')    