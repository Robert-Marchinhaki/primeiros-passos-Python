menor = 0
maior = 0

for p in range(1, 6):
    peso = float(input(f'Digite o {p}° peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}Kg\n'
      f'O menor peso lido foi {menor}Kg')







# # Maior peso e Menor peso
#
#
# cont = 0
#
# for peso in range(1, 6):
#     p = float(input(f'Digite o peso da {peso}° pessoa: '))
#     cont += 1
#     if cont == 1:
#         peso1 = p
#     elif cont == 2:
#         peso2 = p
#     elif cont == 3:
#         peso3 = p
#     elif cont == 4:
#         peso4 = p
#     elif cont == 5:
#         peso5 = p
#     else:
#         print('ERROR!')
#
# if peso1 > peso2 and peso1 > peso3 and peso1 > peso4 and peso1 > peso5:
#     print(f'O maior peso lido foi de: {(peso1)}Kg ')
# elif peso2 > peso1 and peso2 > peso3 and peso2 > peso4 and peso2 > peso5:
#     print(f'O maior peso lido foi de: {(peso2)}Kg ')
# elif peso3 > peso1 and peso3 > peso2 and peso3 > peso4 and peso3 > peso5:
#     print(f'O maior peso lido foi de: {(peso3)}Kg ')
# elif peso4 > peso1 and peso4 > peso2 and peso4 > peso3 and peso4 > peso5:
#     print(f'O maior peso lido foi de: {(peso4)}Kg ')
# elif peso5 > peso1 and peso5 > peso2 and peso5 > peso3 and peso5 > peso4:
#     print(f'O maior peso lido foi de: {(peso5)}Kg ')
# else:
#     print('Erro!')
#
# if peso1 < peso2 and peso1 < peso3 and peso1 < peso4 and peso1 < peso5:
#     print(f'O menor peso lido foi de: {(peso1)}Kg ')
# elif peso2 < peso1 and peso2 < peso3 and peso2 < peso4 and peso2 < peso5:
#     print(f'O menor peso lido foi de: {(peso2)}Kg ')
# elif peso3 < peso1 and peso3 < peso2 and peso3 < peso4 and peso3 < peso5:
#     print(f'O menor peso lido foi de: {(peso3)}Kg ')
# elif peso4 < peso1 and peso4 < peso2 and peso4 < peso3 and peso4 < peso5:
#     print(f'O menor peso lido foi de: {(peso4)}Kg ')
# elif peso5 < peso1 and peso5 < peso2 and peso5 < peso3 and peso5 < peso4:
#     print(f'O menor peso lido foi de: {(peso5)}Kg ')
# else:
#     print('Erro!')

# print(peso1, peso2, peso3, peso4, peso5)