# VERSÃO 2.0 DO EX035.PY (TRIÂNGULOS)

print('Teste os 3 tipos diferentes de triângulos:\n'
      '\n1° Escaleno onde todos os lados possuem diferentes medidas.'
      '\n2° Isósceles que é quando dois lados possuem a mesma medida.'
      '\n3° Equilátero que é quando todos os lados são congruentes (possuem a mesma medida).\n')

r1 = float(input('\033[4;30;45mDigite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo do tipo', end='')
    if r1 == r2 and r2 == r3:
        print(' EQUILÁTERO')
    elif r1 != r2 and r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓCELES')
else:
    print('Os segmentos não podem formar um triângulo')



'''# EXERCICIO FEITO PELO PROFESSOR

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo do tipo', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓCELES')
else:
    print('Os segmentos não podem formar um triângulo')
'''