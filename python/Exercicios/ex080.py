# valores = []
#
# for numeros in range(0, 5):
#     digitado = int(input(f'Digite o {numeros + 1}° número: '))
#     if numeros == 0 or digitado > valores[-1]:
#         valores.append(digitado)
#         print('Valor adicionado no final da lista')
#     else:
#         if digitado < valores[0]:
#             valores.insert(0, digitado)
#             print('Valor adicionado na posição 0')
#         elif valores[0] < digitado < valores[1]:
#             valores.insert(1, digitado)
#             print('posição 1')
#         else:
#             valores.insert(3, digitado)
#             print('Valor adicionado na posição 3')
# print(f'Em ordem seus valores ficarão assim: {valores}')

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados ordenadamente foram: {lista}')