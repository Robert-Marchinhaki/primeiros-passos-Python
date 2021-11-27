def numeric(num):
    num = str(input('Digite um número: ')).strip()
    while num == '' or num:
        print('Erro! Digite um número válido.')
        num = str(input('Digite um número: ')).strip()
        if num.isnumeric():
            break
    return num


n = numeric('Digite um número: ')
print(f'Você digitou o valor {n}')
