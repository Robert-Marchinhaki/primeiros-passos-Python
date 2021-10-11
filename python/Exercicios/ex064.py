# TRATANDO VÁRIOS VALORES V 1.0

n = int(input('Digite um número: '))
s = 0
cont = 0
while n < 999:
    s += n
    n = int(input('Digite um número: '))
    cont += 1
print(f'A soma de todos o números que você digitou é: {s},'
      f'\nvocê digitou {cont} números')
