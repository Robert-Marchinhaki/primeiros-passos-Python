# Somando números, exceto os que são ímpares

soma = 0
for n in range(1, 7):
    number = int(input(f'Digite o {n}° número: '))
    if number % 2 == 0:
        soma += number
print(f'A soma de todos os números pares é: {soma}')