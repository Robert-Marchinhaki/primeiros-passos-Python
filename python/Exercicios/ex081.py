numeros = list()

while True:
    numeros.append(int(input('Digite os valores: ')))
    parada = str(input('Quer continuar [S/N]? ')).upper().strip()
    while parada not in 'SN':
        parada = str(input('Quer continuar [S/N]? ')).upper().strip()
    if parada in 'N':
        break

# Quantos números foram digitados
print(f'No total você digitou {len(numeros)} ', end='')
if len(numeros) == 1:
    print('número')
else:
    print('números')

# Lista em forma ordenada decrescente
numeros.sort(reverse=True)
print(numeros)

# Verificar se o número 5 está na lista
for posicao, v in enumerate(numeros):
    if 5 in numeros and 5 in numeros[v]:
        print(f'O número 5 está na lista na posição {posicao}')
    else:
        print('O número 5 não está na lista')
