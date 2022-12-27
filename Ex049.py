# Refaça o desafio 09, mostrando a tabuada de um número que o 
# usuário escolher, só que agora utilizando laço for.
n = int(input('Digite a tabuada desejada: '))
for i in range(1, 11):
    print(f'{n} x {i:2} = {n*i}')