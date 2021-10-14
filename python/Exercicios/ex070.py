# ESTATÍSTICAS EM PRODUTOS

totalg = pmc = pmb = qdpr = 0  # pmc = produto mais caro; pmb = produto mais barato
# qdpr = quantidade de produto registrado
npmb = ''       # nome do produto mais barato

while True:
    precop = float(input('Preço: '))
    nomep = str(input('Produto: '))
    user = str(input('Tem mais produtos [S/N]: ')).upper().strip()[0]
    while user not in 'SN':
        user = str(input('Tem mais produtos [S/N]: ')).upper().strip()[0]
    # Valor total da compra
    totalg += precop
    # Encontrando o produto mais barato
    if pmb == 0:
        pmb = precop
    if precop < pmb:
        pmb = precop
        npmb = nomep

    # Quantos produtos custam mais de 1000R$
    if precop > 1000:
        qdpr += 1

    # stop
    if user in 'Nn':
        break

print(f'\nO produto mais barato foi {npmb} e ele custa {pmb:.2f}R$'
      f'\n{qdpr} produto(s) custam mais de 1.000R$'
      f'\nO valor total da compra foi de {totalg:.2f}R$')


