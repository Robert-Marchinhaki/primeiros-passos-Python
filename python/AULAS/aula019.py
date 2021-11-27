pessoas = []
cadastro = {}

while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['idade'] = int(input('Idade: '))
    cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while cadastro['sexo'] not in 'FM':
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    pessoas.append(cadastro.copy())
    parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while parada not in 'NS':
        parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if parada in 'N':
        break

for e in pessoas:
    for k, v in e.items():
        print(f'{k} é {v}', end=' ')
    print()
