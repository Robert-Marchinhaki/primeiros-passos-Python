# CONVERSOR DE NÚMERO BINARIO, OCTAL E HEXADECIMAL

print('1 converte para binário, 2 converte para octal e 3 converte para hexadecimal.')
number = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha um número de 1 a 3 para realizar uma conversão: '))

binario = ''
octal = ''
hexadecimal = ''
if escolha == 1:
    binario = format(number, 'b')
    print(f'Seu número inteiro em binário vai ficar assim {binario}')
elif escolha == 2:
    octal = format(number, 'o')
    print(f'Seu número inteiro em octal vai ficar assim {octal}')
elif escolha == 3:
    hexadecimal = format(number, 'x')
    print(f'seu numero inteiro em hexadecimal vai ficar assim {hexadecimal}')
else:
    print('Desculpe, não conseguimos fazer a conversão.')

# EXERCICIO FEITO PELO PROFESSOR

'''num = int(input('Digite um número inteiro: '))
print(Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL)
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')'''