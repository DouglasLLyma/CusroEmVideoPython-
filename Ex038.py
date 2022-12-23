# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela a seguinte mensagem:
# O Primeiro Valor é maior 
# O segundo Valor é maior 
# Não existe valor maior, os dois são iguais. 
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O primeiro valor é Maior!')

elif n2 > n1:
    print('O segundo valor é Maior!')

else:
    print('Não existe valor maior, os dois números são iguais!')
