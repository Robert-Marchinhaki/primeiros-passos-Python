# ALISTAMENTO

from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
sexo = str(input('Informe seu sexo (m ou f): '))

ano = date.today().year
alistamento = ano - nascimento
tempor = 18 - (ano - nascimento)

# print(f'{ano}')
# print(f'{tempor}')
# print(f'{alistamento}')

if sexo == 'f' or sexo == 'feminino':
    print('No caso das mulheres, o alistamento não é obrigatório, e a forma de ingressar é através de concursos e de '
          'voluntariado. Para entrar, a mulher deve ser maior \nde 18 anos e saber que irá servir às forças armadas por'
          ' tempo limitado, já pré-estabelecido. No caso de desejar seguir carreira, deverá prestar concurso \npúblico.')
elif nascimento > ano:
    print('ERRO! Por favor, coloque uma data válida.')
elif alistamento == 18:
    print(f'Você já pode se alistar!')
elif alistamento > 18:
    print(f'Caso ainda não tenha se alistado, se aliste o mais rápido o possível, pois, faz {-tempor}'
          f' ano(s) que você deveria ter se alistado, '
          f'você pode ser \nmultado ou perder suas chances de conseguir um emprego, entre outras coisas.')
elif alistamento < 18:
    print(f'Você ainda não completou os dezoito anos. Falta {tempor} ano(s) até que você possa se alistar.')

# and sexo == 'masculino' or sexo == 'm'
# and sexo == 'masculino' or sexo == 'm'

'''from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda falta {saldo} ano(s) para o seu alistamento.')
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado à {saldo} ano(s).')
    print(f'Seu alistamento foi em {ano}')'''