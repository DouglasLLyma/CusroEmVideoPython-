# Desenvolva um programa que leia o comprimento de três retas 
# e dia ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de Triângulo')
print('-='*20)


r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar Triângulo!')
else:
    print('Os segmentos acima não podem formar Triângulo!')    