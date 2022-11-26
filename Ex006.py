# Crie um algoritmo que leia um número 
# e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
n1 = n * 2
n2 = n * 3
raiz = n**(1/2)
print(f'o número é: {n} \nO dobro é: {n1} \nO seu triplo é: {n2} \nE sua Raiz é: %.2f'%(raiz))
