# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
# 1 para binário 
# 2 para octal 
# 3 para hexadecimal 
# Bases númericas/ Como manipular números / Sistema Binário 
num = int(input('Digite um numero: '))
print('''----------------
[1] Binário
[2] Octal
[3] Hexadecimal
[x] Sair''')
print('------' * 16)

opcao = int(input('Qual a sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num) [2:]}')     
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num) [2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num) [2:]}')         
else:
    print('Opção inválida, Tente novamente!')