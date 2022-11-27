# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço com 5% de desconto. 
produto = float(input('Valor do produto: '))
desconto = (5*produto)/100
valor = produto - desconto
print(f'O valor com 5% de desconto é {valor}')