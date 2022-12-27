# Desenvolva um programa que leia o primeiro termo e a razão 
# de uma PA. No final, mostre os 10 primeiros termos dessa 
# progressão.
pa = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = pa + (10 - 1) * razao
for i in range(pa, decimo + razao, razao):
    print(f'{i}', end=' -> ')
print('ACABOU')