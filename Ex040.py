# Crie um programa que leia duas notas de um aluno e calcule sua 
# média, mostrando uma mensagem no final, de acordo com a média 
# atingida:
# Média a baixo de 5.0:
# Reprovado 
# Média entre 5.0 e 6.9:
# Recuperação
# Média 7.0 ou superior:
# Aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'Entre {n1:.1f} e {n2:.1f} a média é {media:.1f}!')
    print('Reprovado!')
elif media == 5.0 or media < 6.9:
    print(f'Entre {n1:.1f} e {n2:.1f} a média é {media:.1f}!')
    print('Recuperação!') 
elif media <= 7:
    print(f'Entre {n1:.1f} e {n2:.1f} a média é {media:.1f}!')
    print('Aprovado!')      