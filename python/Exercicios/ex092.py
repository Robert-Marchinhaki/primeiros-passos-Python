import datetime

trabalhador = {}

nome = str(input('Nome: '))

# pegar a idade
data_hora = datetime.datetime.now()
date = data_hora.date()
ano_atual = date.strftime("%Y")
ano_nascimento = int(input('Informe seu ano de nascimento: '))
while ano_nascimento > int(ano_atual):
    ano_nascimento = int(input(f'O ano de nascimento não pode ser superior ao ano atual [{ano_atual}]: '))
idade = int(ano_atual) - ano_nascimento

# verificando se possui carteira de trabalho
info_carteira_trabalho = str(input('Tem carteira de trabalho? [S/N]: ')).upper().strip()
while info_carteira_trabalho not in 'SN':
    info_carteira_trabalho = str(input('Responda apenas com [S/N]: ')).upper().strip()
if info_carteira_trabalho in 'N':
    carteira_trabalho = 'Não tem carteira de trabalho'
else:
    carteira_trabalho = int(input('Informe o número da sua carteira de trabalho: '))
    ano_contratacao = int(input('Informe o ano em que foi contratado: '))
    while ano_contratacao > int(ano_atual):
        ano_contratacao = int(input(f'O ano de contração tem que ser menor que o ano atual [{ano_atual}]: '))
    salario = float(input('Informe seu sálario: '))


# pegar ano de aposentadoria
ano_contribuicao = int(ano_atual) - ano_contratacao
ano_aposentadoria = idade - ano_contribuicao + 35

trabalhador['nome'] = nome
trabalhador['idade'] = idade
trabalhador['N° carteira de trabalho'] = carteira_trabalho
trabalhador['salario'] = salario
trabalhador['ano em que foi contratado'] = ano_contratacao
trabalhador['idade em que vai se aposentar'] = ano_aposentadoria
print('-'*30)
for k, i in trabalhador.items():
    print(f'{k}: ', end='')
    print(f'{i}')
    print('-='*25)
