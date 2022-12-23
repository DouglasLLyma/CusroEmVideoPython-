# A confederação nacional de natação precisa de um programa que 
# leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# Até 9 anos:  MIRIM 
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR 
# Até 25 anos: SENIOR 
# Acima:       MASTER 
from datetime import date 
atual = date.today().year
nascimento = int(input('Digite o ano de Nascimento: '))
idade = atual - nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MIRIM!')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classficação: INFANTIL!')    
elif idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: JUNIOR!')    
elif idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: SENIOR!')
else:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: MASTER!')  
          
