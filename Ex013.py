# Faça um algoritmo que leia o salário de um funcionário e mostre 
# seu novo salário com 15% de aumento.
salario = float(input('Salario atual: '))
porcentagem = (salario*15)/100
novoSalario = porcentagem + salario
print(f'O salário com reajuste é R${novoSalario:,.2f}')