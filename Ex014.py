# Escreva um programa que converta uma temperatura 
# digitada em °C e converta para °F.

celsius = float(input('Informe a temperatura em °C: '))
fahreneit = (celsius*1.8)+32
print(f'A temperatura de {celsius:.1f}°C corresponde a {fahreneit:.1f}°F!')