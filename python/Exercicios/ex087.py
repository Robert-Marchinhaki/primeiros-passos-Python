matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_terceira_coluna = maior_segunda_linha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
        if matriz[1][0] != 0:
            maior_segunda_linha = matriz[1][0]
        if matriz[1][coluna] > maior_segunda_linha:
            maior_segunda_linha = matriz[1][coluna]
        soma_terceira_coluna += matriz[linha][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é {maior_segunda_linha}')