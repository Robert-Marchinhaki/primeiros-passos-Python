grupo_pessoas = []
pessoas = {}
med_idade_grupo = 0
mulheres = []
p_acima_media = []

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M/O]: ')).upper().strip()
    while sexo not in 'FMO':
        print('Erro! Use somente [F/M/O].')
        sexo = str(input('Sexo [F/M/O]: ')).upper().strip()
    if sexo in 'F':
        mulheres.append(nome)
    pessoas['nome'] = nome
    pessoas['idade'] = idade
    pessoas['sexo'] = sexo
    grupo_pessoas.append(pessoas.copy())
    med_idade_grupo += idade
    parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-=' * 20)
    while parada not in 'SN':
        print('Erro! Use somento [S/N].')
        parada = str(input('Quer continuar? [S/N]: ')).upper().strip()
        print('-=' * 20)
    if parada in 'N':
        break
med_idade_grupo /= len(grupo_pessoas)
for c in range(0, len(grupo_pessoas)):
    if grupo_pessoas[c]['idade'] > med_idade_grupo:
        p_acima_media.append(grupo_pessoas[c]['nome'])
print('-=' * 20)
print(grupo_pessoas)
print(f'Ao todo {len(grupo_pessoas)} pessoas foram cadastradas')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'A média de idade do grupo é {med_idade_grupo}')
print(f'As pessoas que tem idade acima da média são: {p_acima_media}')
print(pessoas)
