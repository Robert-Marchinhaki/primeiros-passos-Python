# boletim = []
# alunos = []
# notas = []
# media = []
#
# while True:
#     alunos.append(str(input('Nome: ')))
#     notas.append(float(input('Nota 1: ')))
#     notas.append(float(input('Nota 2: ')))
#     alunos.append(notas[:])
#     boletim.append(alunos[:])
#     notas.clear()
#     alunos.clear()
#     parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
#     while parada not in 'SN':
#         parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
#     if parada in 'N':
#         break
#
# print(f'Nº  NOME        MÉDIA')
# print('-'*25)
# for m, s in enumerate(boletim):
#     print(f'{m}  {s[0]:<13}', end='')
#     print(f'{(s[1][0] + s[1][1]) / 2:.1f}')
# print()
# while True:
#     nota_aluno = int(input('Digite o número do aluno: '))
#     for pos in range(0, len(boletim)):
#         if nota_aluno == pos:
#             print(f'O aluno {boletim[nota_aluno][0]} tem notas: {boletim[nota_aluno][1]}')
#     print()
#     parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
#     while parada not in 'SN':
#         parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
#     if parada in 'N':
#         break

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if parada in 'N':
        break

print('-='*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    notas_completas = int(input('Para ver as notas, informe o número do aluno: '))
    if notas_completas <= len(ficha) - 1:
        print(f'Notas de {ficha[notas_completas][0]} são {ficha[notas_completas][1]}')
    parada2 = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if parada2 in 'N':
        print('FINALIZANDO...')
        break
print('<<< VOLTE SEMPRE >>>')
