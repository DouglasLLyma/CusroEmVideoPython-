# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint


print('='*20)
print('----- Jokenpô -----')
print('''Escolha:
[1] = Pedra 
[2] = Tesoura
[3] = Papel
''')
escolha = int(input('Qual a sua escolha? '))
maquina = randint(1,3)
print(maquina)
print(escolha)
if escolha >= 1 and escolha <= 3:
    if escolha != maquina: 
        if escolha == 1 and maquina == 2 or escolha == 2 and maquina == 3 or escolha == 3 and maquina == 1:
            print('Você venceu!')
            if escolha == 1 and maquina == 2:
                print('Pedra quebra Tesoura!')
            elif escolha == 2 and maquina == 3:
                print('Tesoura corta Papel!')
            elif escolha == 3 and maquina == 1:
                print('Papel embala Pedra!')        
        else:
            print('Você Perdeu!!!') 
            if maquina == 1 and escolha == 2:
                print('Pedra quebra Tesoura!')
            elif maquina == 2 and escolha == 3:
                print('Tesoura corta Papel!')
            elif maquina == 3 and escolha == 1:
                print('Papel embala Pedra!')            
    else:
        print('Empate!!! Jogue Novamente.') 
else:
    print('Escolha inválida, tente novamente!')                