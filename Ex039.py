# Faça um programa que leia a ano de nascimento de um jovem e 
# informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é hora de se alistar.
# Se já passou da hora de se alistar.
# Seu programa também deverá mostrar o tempo que falta ou que 
# passou do prazo.
from datetime import date 
atual = date.today().year
sexo = int(input('''
Qual o seu sexo ?
[1] Masculino.
[2] Feminino.
Digite uma das opções: ''')) 

if sexo == 1 :
    nasc = int(input('Ano de Nascimento: '))
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}!')
    if idade == 18:
        print('Você deve se alsitar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        alistamento = nasc + 18
        print(f'Ainda faltam {saldo} anos para o alistamento! ')
        print(f'Seu alistamento será em {alistamento}!')
    else:
        saldo = idade - 18
        alistamento = nasc + 18
        print(f'Você já deveria ter se alistado há {saldo} anos!')
        print(f'Seu alistamento foi em {alistamento}!')
elif sexo == 2:
    print('O alistamento para mulheres não é obrigatório no Brasil!')                        

else:
    print('Opção incorreta, tente novamente!')