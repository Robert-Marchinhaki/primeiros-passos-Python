# VERIFICANDO SE EXISTE A POSSIBILIDADE DE FORMAR UM TRIÂNGULO

reta1 = int(input('Digite o valor da primeira reta: '))
reta2 = int(input('Digite o valor da segunda reta: '))
reta3 = int(input('Digite o valor da terceira reta: '))
a = reta1 + reta2
b = reta1 + reta3
c = reta3 + reta2
if a > reta3:
    print('Estamos verificando...')
if a > reta2:
    print('Aguarde...')
if c > reta1:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo.')

# EXERCICIO FEITO PELO PROFESSOR
#
# r1 = float(input('Digite o valor da primeira reta: '))
# r2 = float(input('Digite o valor da segunda reta: '))
# r3 = float(input('Digite o valor da terceira reta: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os segmentos podem formar um triângulo')
# else:
#     print('Os segmentos não podem formar um triângulo')