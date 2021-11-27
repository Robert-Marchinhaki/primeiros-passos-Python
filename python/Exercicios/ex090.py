situacao = {'nome': str(input('Nome: ')), 'media': float(input('Informe a média do aluno: '))}

if situacao['media'] < 7:
    situacao['situação'] = 'Reprovado'
else:
    situacao['situação'] = 'Aprovado'

for k, v in situacao.items():
    print(f'{k} é igual a {v}')
