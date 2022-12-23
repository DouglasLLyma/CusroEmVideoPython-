# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela 
# a baixo:
# Abaixo de 18.5: Abaixo do Peso 
# Entre 18.5 e 25: Peso ideal 
# 25 até 30: Sobrepeso 
# 30 Até 40: Obesidade 
# Acima de 40: Obesidade Mórdida
peso = float(input('Digite seu peso:(Kg) '))
altura = float(input('Digite sua altura:(m) '))
imc = peso / (altura**2)  
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é de {imc:.1f}, Seu peso é ideial!')
elif 25 <= imc <= 30:
    print(f'Seu IMC é de {imc:.1f}, você está em Sobrepeso!')
elif 30 <=  imc <= 40:
    print(f'Seu IMC é de {imc:.1f}, você está em Obesidade!')
else:
    print(f'Seu IMC é de {imc:.1f}, você está com Obsidade Morbida!') 

