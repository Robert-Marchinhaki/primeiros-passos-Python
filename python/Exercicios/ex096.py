def area(largura, comprimento):
    print(f'A área do seu tereno ({largura} x {comprimento}) é de {largura * comprimento}m²')


print(' Controle de Terrenos ')
print('-' * len(' Controle de Terrenos '))
larg = float(input('Largura: m'))
comp = float(input('Comprimento: m'))
area(largura=larg, comprimento=comp)
