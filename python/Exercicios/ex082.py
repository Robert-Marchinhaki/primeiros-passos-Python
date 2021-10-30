mynumber = list()
pares = list()
impares = list()


while True:
    digitado = int(input('Digite os valores: '))
    mynumber.append(digitado)
    if digitado % 2 == 0:
        pares.append(digitado)
    else:
        impares.append(digitado)
    parada = str(input('Deseja continua[S/N]? ')).upper().strip()
    while parada not in 'SN':
        parada = str(input('Deseja continua[S/N]? ')).upper().strip()
    if parada not in 'S':
        break

print(f'Você digitou os seguintes números: {mynumber}')
print(f'Os seguintes números PARES foram digitados: {pares}')
print(f'Os seguintes números ÍMPARES foram digitados: {impares}')