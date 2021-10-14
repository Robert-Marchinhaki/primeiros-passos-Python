# PROGRAMA PARA LER IDADE E SEXO DE VÁRIAS PESSOAS

homem = mulher = contador = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Não entendi. Digite novamente [M/F]: ')).upper().strip()[0]
    cadastro = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    while cadastro not in 'SN':
        cadastro = str(input('Não entendi. Digite novamente: [S/N] ')).upper().strip()[0]
    # QUANTAS PESSOAS TEM MAIS DE 18 ANOS
    if cadastro in 'S':
        if idade > 18:
            contador += 1
        # QUANTOS 'HOMENS' FORAM CADASTRADOS
        if sexo in 'M':
            homem += 1
        # QUANTAS 'MULHERES' TEM MENOS DE 20 ANOS
        if sexo in 'F' and idade < 20:
            mulher += 1
    else:
        if idade > 18:
            contador += 1
        if sexo in 'M':
            homem += 1
        if sexo in 'F' and idade < 20:
            mulher += 1
        break

print(f'\n{contador} pessoa(s) tem mais de 18 anos'
      f'\n{homem} homem/homens foi/foram cadastrado(s)'
      f'\n{mulher} mulher(es) tem menos de 20 anos')
