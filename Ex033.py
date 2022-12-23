# Faça um programa que leia três números e mostre 
# qual é o maior 
# e qual é o menor.


a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

#Verificando quem é menor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c   
print(f'O menor valor é {menor}!')    

#Verificando o maior valor digitado
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor é {maior}!')        
