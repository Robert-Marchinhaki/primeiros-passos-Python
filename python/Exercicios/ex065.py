# programa para ler vários números e dizer a média, o maior e o menor valor digitado


r = 'S'
soma = cont = med = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
med = soma / cont
print('Você digitou', cont, 'números. A soma entre eles é:', soma, 'E a média é:', med)
print('O maior valor é', maior, 'e o menor valor é', menor)
