# Faça um programa que leia um número 0 a 9999
# e mostre na tela cada um dos digitos separados.
# ex:
# digite um número:1834
# unidade:4
# dezena:3
# centenas:8
# milhar:1
num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 
print(f'Unidade: {u}\nDezena: {d}\nCentena: {c}\nMilhar: {m}')
    