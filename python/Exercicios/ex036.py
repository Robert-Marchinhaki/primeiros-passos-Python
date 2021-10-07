# APROVANDO EMPRÉSTIMO

casa = float(input('Digite o valor da casa: '))
salario = float(input('Informe quantos você recebe: '))
parcela = int(input('Informe em quantas vezes quer pagar: '))

tsal = salario * (30 / 100)
parcasa = casa / parcela
valorp = parcasa
if parcela <= 12:
    valorp = valorp + (valorp * (5.88 / 100))
elif parcela <= 24:
    valorp = valorp + (valorp * (8.00 / 100))
else:
    valorp = valorp + (valorp * (10.50 / 100))
if tsal < valorp:
    print('Empréstimo NEGADO.')
elif valorp < tsal:
    print('Empréstimo APROVADO.')

print(f'Se você for pagar em {parcela} vezes vai custar {valorp:.2f}R$ por mês')


# EXERCICIO FEITO PELO PROFESSOR

'''casa = float(input('Valor da casa: R$'))
salario = float(input('Informe seu sálario: R$'))
anos = int(input('Quantos anos de financimento: anos'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de {casa:.2f}R$ em {anos} anos,'
      f' a prestação será de {prestacao}')
if prestacao <= minimo:
      print('Empréstimo APROVADO!')
else:
      print('Empréstimo NEGADO!')'''