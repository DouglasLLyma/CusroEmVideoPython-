# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária 
# para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m².
altura = float(input('Digite a altura: '))
comprimento = float(input('Digite a laugura: '))
area = altura * comprimento
tinta = area / 2
print(f'A parede tem {comprimento} de largura e {altura} de altura, e você vai usar {tinta} litros de tinta.')