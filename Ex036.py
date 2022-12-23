#  Escreva um programa para aprovar o empréstimo bancário para a 
#  compra de casa. O programa vai perguntar o valor da casa, e 
#  salário do comprador e em quantos anos ele vai pagar.
#  Calcule o valor da prestação mensal, sabendo que ela não pode
#  exceder 30% do salário ou então o emprestimo será negado.
casa = float(input('Qual o valor da casa R$: '))
salario = float(input('Qual é o seu salário R$: '))
ano = int(input('Em quantos anos de financimento: '))

prestacao = (casa / (ano * 12))  
analise = salario * 30 / 100

if prestacao <= analise:
    print('Emprestimo Aprovado!')
    print(f'Você vai Pagar {ano*12} parcelas no valor de R${prestacao:.2f}')
    
else:
    print('Negado')
  
