# Faça um programa que leia um número qualque e 
# mostre na tela sua tabuada.
numero = int(input('Digite um número: '))
print('-'*12)
print(  '{} x 1  = {}\n'
        '{} X 2  = {}\n'
        '{} X 3  = {}\n'
        '{} x 4  = {}\n'
        '{} X 5  = {}\n'
        '{} X 6  = {}\n'
        '{} X 7  = {}\n'
        '{} X 8  = {}\n'
        '{} X 9  = {}\n'
        '{} X 10 = {}\n'
        .format( numero, numero*1
                ,numero, numero*2
                ,numero, numero*3
                ,numero, numero*4
                ,numero, numero*5
                ,numero, numero*6
                ,numero, numero*7
                ,numero, numero*8
                ,numero, numero*9
                ,numero, numero*10)) 
print('-'*12)                