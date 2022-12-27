# Faça um programa que calcule a soma entre todos os números 
# impares que são múltiplos de três e que se encontram no 
# intervalo de 1 até 500. 

soma = 0
cont = 0
for intervalo in range(1, 501, 2):
    if intervalo % 3 == 0:
        soma += intervalo 
        cont += 1
print(f'A soma de todos os {cont} solicitados  é {soma}!')         


    
    
    
    