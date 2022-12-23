# Faça o desafio 35 dos triângulos, acrescentando o recurso de 
# mostrar que tipo de triângulo será formado.
# Equilátero: todos os lados iguais 
# Isósceles: dois lados iguais 
# Escaleno: todos os lados diferentes 
r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('Segundo Seguimento: '))
r3 = float(input('Terceiro Seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um Triângulo. ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')        
else:
    print('Não é possível formar um triângulo!')     
