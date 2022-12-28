# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas já são maiores.
from datetime import date
hoje = date.today().year 
cont = 0
cont1 = 0
for ano in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento {ano}°: '))
    maioridade = hoje - nasc
    if maioridade >= 18:
        cont += 1
        
    else:
        cont1 += 1    
        
print(f'Nesse lista existem {cont} pessoas maiores de idade e {cont1} menores!')    