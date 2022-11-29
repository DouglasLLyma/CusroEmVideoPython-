# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço com 5% de desconto. 
produto = float(input('Valor do produto R$: '))
desconto = produto - (5*produto)/100
print(f'O valor do produto é R$ {produto:.2f} e com 5% de desconto custa {desconto:.2f}')