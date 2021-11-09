# pessoas = []
# cadastro = []
# cont = maispesadas = maisleves = 0
#
# while True:
#     nome = str(input('Digite seu nome: '))
#     peso = float(input('Informe seu peso: KG'))
#     cont += 1
#     if cont == 1:
#         maispesadas = maisleves = peso
#     else:
#         if maispesadas < peso:
#             maispesadas = peso
#         if maisleves > peso:
#             maisleves = peso
#     cadastro.append(nome)
#     cadastro.append(peso)
#     pessoas.append(cadastro[:])
#     cadastro.clear()
#     parada = str(input('Deseja continuar [S/N]? ')).upper().strip()
#     while parada not in 'SN':
#         parada = str(input('Não entendi! Digite novamente [S/N]: ')).upper().strip()
#     if parada in 'N':
#         break
#
# # quantas pessoas foram cadastradas (pcadastro)
# print(pessoas)
# if len(pessoas) == 1:
#     print(f'Somente {len(pessoas)} pessoa foi cadastrada')
# else:
#     print(f'{len(pessoas)} pessoas foram cadastradas')
#
# # mais pesados e mais leves
# print(f'O maior peso foi de {maispesadas}Kg. Peso de: ', end='')
# for p in pessoas:
#     if p[1] == maispesadas:
#         print(f'{p[0]}', end=', ')
# print(f'\nO menor peso foi de {maisleves}Kg. Peso de: ', end='')
# for p in pessoas:
#     if p[1] == maisleves:
#         print(f'{p[0]}', end=', ')

temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break

print(f'Ao todo você cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
