# NÚMEROS COM FLAG

cont = num = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'{cont} número(s) foram digitados, '
      f'A soma entre esses número é {soma}')
