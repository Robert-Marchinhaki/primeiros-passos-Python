# palavras = ('ROBERT', 'KIANE')
#
# print(f'Na palavra {palavras[0]} temos: ', end='')
# for n in palavras[0]:
#     if n in 'AEIOU':
#         print(f'{n.lower()}', end=' ')
#
# print(f'\nNa palavra {palavras[1]} temos: ', end='')
# for n in palavras[1]:
#     if n in 'AEIOU':
#         print(f'{n.lower()}', end=' ')


palavras = ('robert adrian marchinhaki da silva', 'kiane verbeling dos santos',
            'vinicius smith malec', 'aryane Ladeira da Silva')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
