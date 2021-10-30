num = [1, 5, 0, 8]  # num = list()
# listas são mutáveis
num[2] = 6

# Adicionando o valor 7
num.append(7)
num.append(9)
num.append(10)

# Colocar os números em ordem
num.sort()

# (posição, objeto) posição em que o objeto vai entrar
num.insert(1, 3)
num.insert(1, 2)
num.insert(3, 4)
#num.insert(5, 2)


# removendo um objeto da lista
#num.pop(2)   # remove o último valor (não especificou)
print(num)
print(f'Essa lista tem {len(num)} elementos')
if 10 in num:
    num.remove(10)  # remove apenas a primeira ocorrência
else:
    print('O número não existe')

print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}')

# nesse caso uma lista fica ligada a outra
a = [2, 3, 4, 7]
b = a
b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')
#
# # nesse caso você cria uma cópia da lista A
# a = [2, 3, 4, 7]
# b = a[:]
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')