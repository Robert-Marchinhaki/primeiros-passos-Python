# VERIFICANDO QUAL É O MAIOR NÚMERO E QUAL É O MENOR

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))
maior = num1
if (num2 > maior):
    maior = num2
if (num3 > maior):
    maior = num3
print(f'O maior número é o {maior}')
menor = num1
if (num2 < menor):
    menor = num2
if (num3 < menor):
    menor = num3
print(f'O menor número é o {menor}')


# EXERCICIO FEITO PELO PROFESSOR

# a = int(input('Digite o primeiro número: '))
# b = int(input('Digite o segundo número: '))
# c = int(input('Digite o terceiro número: '))
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# maior = a
# print(f'O menor número é o {menor}')
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# print(f'O maior número é o {maior}')