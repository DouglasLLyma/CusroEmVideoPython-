# Faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artificio, indo de 10 até 0, com 
# uma pausa de 1 segundo entre eles.
from time import sleep

for a in range(10, -1, -1):
    print(a)
    print('*/*')
    sleep(2)
print('*****Feliz Ano Novo*****')    