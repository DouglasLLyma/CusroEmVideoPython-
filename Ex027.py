# Faça um programa que leia o nome completo 
# de uma pessoa, mostrando em seguida o primeiro e o 
# último nome separadamente. 
# Ex: Ana Maria de Souza 
# Primeiro = Ana 
# Último = Souza
nome = str(input('Digite seu nome: ')).strip()
dividir = nome.split()
print(f'Primeiro nome {dividir[0]}')
print('Ultimo nome: {}'.format(dividir[len(dividir)-1]))