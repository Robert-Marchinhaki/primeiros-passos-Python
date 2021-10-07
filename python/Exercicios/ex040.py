# MÉDIA DE NOTA

trismestre1 = float(input('Digite a nota do seu primeiro trimestre: '))
trismestre2 = float(input('Digite a nota do seu segundo trimestre: '))
trismestre3 = float(input('Digite a note do seu terceiro trimestre: '))
notaf = (trismestre1 + trismestre2 + trismestre3) / 3
print(f'sua media final é de {notaf:.1f}')
if notaf < 5.0:
    print('\033[31mREPROVADO!')
elif notaf >= 5.0 and notaf < 6.0:
    print('Você está de \033[33mRECUPERAÇÃO!')
else:
    print('PARABÉNS! Você está \033[32mAPROVADO!')

# DESAFIO FEITO PELO PROFESSOR
''' nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {media}')
if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO!')
elif media < 5:
    print('O aluno está REPROVADO!')
else:
    print('O aluno está APROVADOR!') '''
