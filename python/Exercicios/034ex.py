# AJUSTE SALARIAL DE ACORDO COM A QUANTIDADE GANHA

sal = float(input('Digite seu sálario: '))
aumb = 10 / 100
aumm = 15 / 100
salm = sal * aumb
salb = sal * aumm
resb = sal + salb
resm = sal + salm
aumb = resb - sal
aumm = resm - sal
if (sal > 1250):
    input(f'Seu novo sálario é {resm:.2f}R$. Você ganhou um aumento de {aumm:.2f}')
if (sal <= 1250):
    input(f'Seu novo sálario é {resb:.2f}R$. Você ganhou um aumento de {aumb:.2f}')

# EXERCICIO FEITO PELO PROFESSOR

# salario = float(input('Qual é o salario do funcionario? R$'))
# if salario <= 1250:
#     novo = salario + (salario * 15 / 100)
# else:
#     novo = salario + (salario * 10 / 100)
# print(f'Quem ganhava {salario:.2f}R$ passa a ganhar {novo:.2f}R$')