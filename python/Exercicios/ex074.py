# from random import randint
#
# maior = menor = 0
#
# print('Os valores sorteados foram:', end=' ')
# for cont in range(0, 5):
#     numerosaleatorios = randint(4, 9)
#     numeros = numerosaleatorios
#     print(numeros, end=' ')
#     if cont == 0:
#         maior = menor = numeros
#     if maior < numeros:
#         maior = numeros
#     if menor > numeros:
#         menor = numeros
#
# print(f'\nO maior número sorteado foi: {maior}')
# print(f'O menor número sorteado foi: {menor}')

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: {numeros} \nO maior valor é {max(numeros)} \nO menor valor é {min(numeros)}')
