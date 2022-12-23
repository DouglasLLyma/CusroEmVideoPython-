# Desenvolva um programa que pergunte a distância de uma viagem 
# em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para 
# viagens
# de até 200Km e R$ 0,45 para viagens mais longas.
km = int(input('Qual a distância em km: '))
if km <= 200:
    print(f'Sua passagem custa R${km*0.50:.2f}')
else:
    print(f'Sua Passagem custa R${km*0.45:.2f}')    
