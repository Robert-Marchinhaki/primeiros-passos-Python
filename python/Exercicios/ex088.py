# from random import randint
# numeros = []
# numeros_sorteados = []
# jogos_gerados = 0
# quantidade_jogos_requisitados = int(input('Quantos jogos deseja gerar: '))
# print()
# while True:
#     jogos_gerados += 1
#     for sorteio in range(0, 6):
#         numeros_sorteados.append(randint(1, 60))
#         if numeros_sorteados not in numeros:
#             numeros.append(numeros_sorteados[:])
#             numeros_sorteados.clear()
#         else:
#             while numeros_sorteados in numeros:
#                 numeros_sorteados.clear()
#                 numeros_sorteados.append(randint(1, 60))
#                 if numeros_sorteados not in numeros:
#                     numeros.append(numeros_sorteados[:])
#                     numeros_sorteados.clear()
#     print(f'Jogo {jogos_gerados}: [', end='')
#     for c, v in enumerate(numeros):
#         print(f'{numeros[c][:]}', end='')
#     print(']')
#     numeros.clear()
#     if quantidade_jogos_requisitados == jogos_gerados:
#         break

from random import randint
from time import sleep
jogos_temporarios = []
jogos_permanentes = []
cont = 0
num_jogos = int(input('Quantos jogos deseja sortear? '))
for c in range(0, num_jogos):
    while True:
        num_sorteados = randint(1, 60)
        if num_sorteados not in jogos_temporarios:
            jogos_temporarios.append(num_sorteados)
            cont += 1
        if cont >= 6:
            break
    jogos_permanentes.append(jogos_temporarios[:])
    jogos_temporarios.clear()
    cont = 0
print('-='*5, 'SEUS JOGOS', '=-'*5)
for jogo, lista in enumerate(jogos_permanentes):
    print(f'Jogo {jogo + 1}: {lista}')
    sleep(1)
print('-='*5, 'BOA SORTE', '=-'*5)