# VEFICANDO QUAL NÚMERO É MAIOR OU SE SÃO IGUAIS

number1 = int(input('Digite um número inteiro: '))
number2 = int(input('Digite outro número inteiro: '))

if number1 > number2:
    print(f'O primeiro valor é maior ({number1})')
elif number1 < number2:
    print(f'O segundo valor é maior ({number2})')
else:
    print(f'Não existe valor maior, os dois são iguais ({number1} {number2})')


# EXERCICIO FEITO PELO PROFESSOR

'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior')
elif n2 > n1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')'''