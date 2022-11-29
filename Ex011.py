# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária 
# para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m².
altura = float(input('Digite a altura: '))
largura = float(input('Digite a laugura: '))
area = altura * largura
tinta = area / 2
print(f'A parede tem {largura}m de largura e {altura}m de altura.\nTotalizando {area}m².\nVocê precisa de {tinta}L de tinta para pintar esse espaço.')