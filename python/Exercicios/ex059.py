# MENU DE OPÇÕES

print(''' Escolha baseado nas opções abaixo:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] digitar novos números
[ 5 ] sair do programa
''')

op = 1
while op != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    op = int(input('Escolha uma opção: '))
    if op == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif op == 2:
        soma = n1 * n2
        print(f'{n1} x {n2} = {soma}')
    elif op == 3:
        if n1 < n2:
            print(f'{n2} é maior')
        elif n1 == n2:
            print('Os dois números são iguais')
        else:
            print(f'{n1} é maior')
    elif op == 4:
        print('Digite novamente.')
    else:
        print('Por favor, digite um número que esteja dentro das opções citadas acima.')
