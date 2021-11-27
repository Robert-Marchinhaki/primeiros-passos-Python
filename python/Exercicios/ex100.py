from random import randint


def soma_par():
    soma = 0
    print('O valores sorteados foram: ', end='')
    for valor in numeros:
        print(valor, end=' ')
        if valor % 2 == 0:
            soma += valor
    print()
    print(f'Somando somente o pares temos: {soma}')


numeros = []
for c in range(0, 5):
    numeros.append(randint(1, 6))
soma_par()
