# V 2.0 PA (ex061)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
qtermo = int(input('Digite a quantidade de termo: '))

m = 0
while m <= qtermo:
    m += 1
    print(f'O {m}° termo é {termo}')
    termo += razao
    if m == qtermo:
         qtermo = int(input('Digite novos termos: '))