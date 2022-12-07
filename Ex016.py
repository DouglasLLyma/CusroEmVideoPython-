# Crie um programa que leia um número real qualquer pelo 
# teclado e mostre na tela a sua porção inteira.
from math import trunc 
num = float(input('Digite um número: '))
var = trunc(num)
print(f'O número é {num} e sua porção inteira é {var}.')