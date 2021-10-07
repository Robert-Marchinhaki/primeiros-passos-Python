# Programa para ler a maioria e dizer quantos são de maior e quantos são de menor
# ou quantos já tem 18 anos

m = 0
i = 0
md = 0

for ano in range(1, 8):
    ida = int(input('Digite sua idade: '))
    if ida > 18:
        # print(f'Você completou 18 anos à {ida - 18} ano(s) atrás.')
        m += 1
    elif ida == 18:
        i += 1
        # print('PARABÉNS!!!')
    else:
        md += 1
        # print(f'Você tem {ida} ano(s) ainda falta {18 - ida} ano(s) para você chegar aos 18 anos.')
print(f'Das 7 pessoas que fizeram o teste {m} tem mais que 18 anos, '
      f'{i} tem 18 anos e {md} tem menos que 18 anos.')
