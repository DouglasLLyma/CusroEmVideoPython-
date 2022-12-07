# Faça um programa que leia o comprimento do cateto 
# oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot 
oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
#hipotenusa = (oposto**2 + adjacente**2) ** (1/2)
hipotenusa = hypot(oposto, adjacente)
print(f'{hipotenusa:.2f}')