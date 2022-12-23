# Elabore um programa que calcule o valor a ser pago por um produto>
# Considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/Cheque: 10% de desconto 
# À vista no cartão: 5% de desconto 
# em até 2x no cartão: preço normal 
# 3x ou mais no cartão: 20% de juros.
print('='*10,'Lojas Lima','='*10)
valor = float(input('Qual o valor do produto R$: '))
print('''Formas de pagamento: 
[1] À VISTA Dinheiro/Cheque.
[2] À VISTA no Cartão.
[3] Em Até 2x no Cartão.
[4] 3x ou Mais no Cartão.''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
    print(f'Sua compra no valor de R${valor:.2f} com desconto de 20%, vai para R${total:.2f}.')
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print(f'Sua compra no valor de R${valor:.2f} com desconto de 5%, vai para R${total:.2f}.')    
elif opcao == 3:
    total = valor / 2
    print(f'total da compra R${valor:.2f}. Parcelada em 2x sem juros no valor de R${total:.2f}.')
elif opcao == 4:
    total = valor + (valor * 20/ 100)
    toparcela = int(input('Quantas Parcelas? '))
    parcela = total / toparcela
    print(f'Sua Compra de R${valor:.2f}, com juros de 20% vai para R${total:.2f}.')
    print(f'Parcelado em {toparcela}x no valor de R${parcela:.2f}.')
else: 
    total = 0
    print('Opção Inválida. Tente Novamente!')        