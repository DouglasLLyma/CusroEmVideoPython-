#Crie um programa que leia o nome completo 
#de uma pessoa e mostre.
# O nome com todas as letras maiúculas 
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem espaços)
# Quantas letras tem o primeiro nome. 
nome = str(input('Digite seu nome: ')).strip()
print(f'Letras Maiúsculas: {nome.upper()}')
print(f'Letras Minúsculas: {nome.lower()}')
print('Quantidade de letras sem espaço: {}'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
