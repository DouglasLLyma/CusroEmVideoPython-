#Manupulando Cadeia de Textos.
frase = 'Curso em Vídeo Python'

print(f'Print: {frase}.')
print(f'Fatiando com um parâmetro, retornado o índice três da frase: {frase[3]}')
print(f'Fatiando com dois parâmetros,1° parâmetro retorna o índice três da frase e o segundo até onde ela termina: {frase[3:13]}')
print(f'Do ínicio até o índice treze: {frase[:13]}')
print(f'Do índice treze até o final: {frase[13:]}')  
print(f'Com dois parâmetros, começo e fim. Pulando de dois em dois: {frase[1:15:2]}')
print('Usando aspas triplas para imprimir textos!')
print("""1.parte da filosofia responsável pela investigação dos princípios 
que motivam, distorcem, disciplinam ou orientam o comportamento humano, 
refletindo esp. a respeito da essência das normas, valores, prescrições e 
exortações presentes em qualquer realidade social.""")
print("Contar quantas vezes aparece a letra o, dentro da frase{}: ".format(frase.count('o')))
print(f'Usando a função len para contar quantos caracteres tem dentro da frase: {len(frase)}')
print(f'Usando Upper para deixar todos os caracteres maiúsculos: {frase.upper()}')
print(f'Usando lower para deixar todas as letras em minúsculo: {frase.lower()}')
print(f'Strip remove os espaços antes e depois da frase: {frase.strip()}')
print('Replace substitui uma string dentro da frase: '.format(frase.replace('Python','Douglas')))
print('Verifique se a plavra curso está dentro da frase: {}'.format('Curso' in frase))
dividido = frase.split()
print(dividido[0])