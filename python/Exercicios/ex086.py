# cont = 0
# matriz_inicial = [[], [], []]
# for c in range(len(matriz_inicial)):
#     digite = int(input(f'Digite um número para a posição {0, c}: '))
#     cont += 1
#     if cont == 1:
#         matriz_inicial[0] = [digite]
#     elif cont == 2:
#         matriz_inicial[1] = [digite]
#     else:
#         matriz_inicial[2] = [digite]
#
# cont = 0
# matriz_secundaria = [[], [], []]
# for c in range(len(matriz_secundaria)):
#     digite = int(input(f'Digite um número para a posição {1, c}: '))
#     cont += 1
#     if cont == 1:
#         matriz_secundaria[0] = [digite]
#     elif cont == 2:
#         matriz_secundaria[1] = [digite]
#     else:
#         matriz_secundaria[2] = [digite]
#
# cont = 0
# matriz_terceiria = [[], [], []]
# for c in range(len(matriz_terceiria)):
#     digite = int(input(f'Digite um número para a posição {2, c}: '))
#     cont += 1
#     if cont == 1:
#         matriz_terceiria[0] = [digite]
#     elif cont == 2:
#         matriz_terceiria[1] = [digite]
#     else:
#         matriz_terceiria[2] = [digite]
#
#
# for c in matrix_inicial:
#     print(c, end='')
# print()
# for c in matrix_secundaria:
#     print(c, end='')
# print()
# for c in matrix_terceiria:
#     print(c, end='')
# print()

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()