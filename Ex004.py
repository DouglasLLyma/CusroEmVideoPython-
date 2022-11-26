#Faça um programa que leia algo pelo teclado e mostre 
#na tela o seu tipo primitivo e todas as informações 
#possiveis sobre ele.
var = input('Digite algo: ')
print('Tipo primitivo:', type(var))
print('É somente espaços: ', var.isspace())
print('É um número:',var.isnumeric())
print('É alfabético: ',var.isalpha())
print('Contém números e letras: ',var.isalnum())
print('Contém só letras Maiúsculas: ',var.isupper())
print('Contém só letras minúsculas: ',var.islower())
print('Está capitalizada: ',var.istitle())



