# VERIFICADOR DE GÊNERO

''' sexo = ''

while sexo == 'M' or 'F':
    sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        print('Próximo.')
    else:
        print('Erro, digite novamente') '''

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Digite novamente: ')).strip().upper()
print(f'{sexo} registrado com sucesso.')
