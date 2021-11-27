from time import sleep


def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.5)
    print()
    print('-=' * 20)


# contador de 1 até 10
print('Contagem de 1 até 10 de 1 em 1')
contador(inicio=1, fim=11, passo=1)


# contador de 10 até 0
print('Contagem de 10 até 0 de 2 em 2')
contador(inicio=10, fim=-1, passo=-2)


# contagem personalizada
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if i > f:
    if p == 0:
        p = 1
        print(f'Contagem de {i} até {f} pulando de {p} em {p}')
        f = f - p
        p = p - p - p
    elif p < 0:
        f = f + p
        print(f'Contagem de {i} até {f-f} pulando de {p} em {p}')
    else:
        f = f - p
        print(f'Contagem de {i} até {f - f} pulando de {p} em {p}')
        p = p - p - p
else:
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    f += 1
contador(inicio=i, fim=f, passo=p)

