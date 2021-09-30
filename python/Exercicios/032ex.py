# VERIFICADOR DE ANO BISSEXTO

'''ano = int(input('Quantos dias tem esse ano: '))
if ano == 365:
    print('Esse ano não é um ano bissexto.')
else:
    print('Esse ano é um ano bissexto.')
'''

ano = float(input('Digite o ano atual: '))
#bis = ano // 4
if (ano%4) == 0:
    print('Esse ano é um ano bissexto')
else:
    print('Esse ano não é um ano bissexto')

# '''EXERCICIO FEITO PELO PROFESSOR'''

# from datetime import date
#
# ano = int(input('Digite o ano que quer analisar ou digite 0 para analisar o ano atual: '))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print(f'O ano {ano} é BISSEXTO')
# else:
#     print(f'O ano {ano} não é BISSEXTO')