# NÚMEROS MÚLTIPLOS DE 3 NO INTERVALO DE 1 A 500


lista = []

for n in range(1, 500, 2):
    if n % 3 == 0:
        lista += [n]


soma = 0
for n in lista:
    print(n)
    soma += n
print('Soma:', soma)
