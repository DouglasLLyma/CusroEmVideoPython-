# Escreva um programa que leia um valor em metros 
# e o exiba convertido em centimetros e milimetros. 
metros = float(input('Digite a quantidade de metros: '))
centrimentos = metros * 100
milimetros = metros * 1000
print(f'Em tantos {metros}m temos {centrimentos:.0f}cm e {milimetros:.0f}mm')