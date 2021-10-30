valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c}° valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'O maior valor digitado foi {maior} nas posições: ', end='')
for indice, numero in enumerate(valores):
    if numero == maior:
        print(f'{indice},', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições: ', end='')
for indice, numero in enumerate(valores):
    if numero == menor:
        print(f'{indice},', end=' ')
