# PA V 2.0

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
m = 0
while m < 10:
    m += 1
    print(f'O {m}° primeiro termo é: {termo}')
    termo += razao
