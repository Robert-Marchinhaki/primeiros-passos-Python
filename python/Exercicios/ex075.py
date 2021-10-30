# numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
#                int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
#
# numnove = numtres = numpar = cont = 0
#
# print(numeros)
#
# if numeros[0] == 9:
#     numnove += 1
#     print(f'O número nove foi digitado {numnove} vezez')
# if numeros[1] == 9:
#     numnove += 1
#     print(f'O número nove foi digitado {numnove} vezes')
# if numeros[2] == 9:
#     numnove += 1
#     print(f'O número nove foi digitado {numnove} vezes')
# if numeros[3] == 9:
#     numnove += 1
#     print(f'O número nove foi digitado {numnove} vezes')
# elif numeros[0] != 9 and numeros[1] != 9 and numeros[2] != 9 and numeros[3] != 9:
#     print('O número nove não foi digitado nenhuma vez')
#
# if 3 == numeros[0]:
#     numtres = 1
#     print(f'\nO número 3 foi digitado pela primeira vez na {numtres}° posição ')
# elif 3 == numeros[1]:
#     numtres = 2
#     print(f'\nO número 3 foi digitado pela primeira vez na {numtres}° posição ')
# elif 3 == numeros[2]:
#     numtres = 3
#     print(f'\nO número 3 foi digitado pela primeira vez na {numtres}° posição ')
# elif 3 == numeros[3]:
#     numtres = 4
#     print(f'\nO número 3 foi digitado pela primeira vez na {numtres}° posição ')
# else:
#     print("O número três não foi digitado em nenhuma posição.")
#
# if numeros[0] % 2 == 0:
#     print('Os números pares são: ', numeros[0], end=' ')
# if numeros[1] % 2 == 0:
#     print(numeros[1], end=' ')
# if numeros[2] % 2 == 0:
#     print(numeros[2], end=' ')
# if numeros[3] % 2 == 0:
#     print(numeros[3])
# if numeros[0] % 2 != 0 and numeros[1] % 2 != 0 and numeros[2] % 2 != 0 and numeros[3] % 2 != 0:
#     print('Nenhum número par foi digitado')

num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os seguintes números: {num}')

# Quantas vezes o número nove apareceu
print(f'O número nove apareceu {num.count(9)} vezes')
# Primeira vez em que o número 3 foi digitado
if 3 in num:
    print(f'O número três apareceu pela primeira vez na {num.index(3)+1}° posição')
# Números pares digitados
else:
    print('O número três não foi digitado')
    print('Os números pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
