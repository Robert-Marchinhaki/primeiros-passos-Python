# parimpar = []
# par = []
# impar = []
#
# for numeros in range(1, 8):
#     digite = int(input(f'Digite o {numeros}° número: '))
#     if digite % 2 == 0:
#         par.append(digite)
#     else:
#         impar.append(digite)
#
# parimpar.append(par[:])
# parimpar.append(impar[:])
# print(f'Os números pares são: {parimpar[0]}'
#       f'\nOs números ímpares são: {parimpar[1]}')

numeros = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são {numeros[0]}')
print(f'Os números ímpares são {numeros[1]}')
