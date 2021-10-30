numeros = list()


while True:
    digitado = (int(input('Digite os valores: ')))
    if digitado not in numeros[:]:
        print('Número adicionado com sucesso...')
    else:
        numeros.remove(digitado)
        print('Erro! Valor já digitado')
    numeros.append(digitado)
    parada = str(input('Quer adicionar mais valores[S/N]? ')).upper().strip()
    while parada not in 'SN':
        parada = str(input('Quer adicionar mais valores[S/N]? ')).upper().strip()
    if 'N' in parada:
        break


numeros.sort()
print(f'Os números digitados foram: {numeros} (estão ordenados)')