'''# GERENCIADOR DE PAGAMENTOS
print('Formas de pagamento: Dinheiro, Cheque, Cartão, ParceladoDuasx, ParceladoTresx')
valorp = float(input('Digite o valor do produto: '))
formapagamento = str(input('Informe a forma de pagamento: '))
dich = valorp - (valorp * (10 / 100))
x1cartao = valorp - (valorp * (5 / 100))
x2cartao = valorp
x3cartao = valorp + (valorp * (20 / 100))
total = ''
# print(f'{dich:.2f}R$'
#       f'\n{x1cartao:.2f}R$'
#       f'\n{x2cartao:.2f}R$'
#       f'\n{x3cartao:.2f}R$')
if valorp == 0:
    print('Por favor, digite um valor.')
elif formapagamento == 'dinheiro':
    total = dich
    print(f'O valor total da compra é {total:.2f}R$')
elif formapagamento == 'Cartao':
    total = x1cartao
    print(f'O valor total da compra é {total:.2f}R$')
elif formapagamento == 'parceladoduasx':
    total = x2cartao
    print(f'O valor total da compra é {total:.2f}R$')
else:
    total = x3cartao
    print(f'O valor total da compra é {total:.2f}R$')'''


# EXERCICIO FEITO PELO PROFESSOR

print(f'\033[4;35m{" LOJAS GUANABARA ":=^40}\033[m\n')
preco = float(input('Preço das compras: R$'))
print(f'''\n\033[4;30;47m{"FORMAS DE PAGAMENTO":■^40}\033[m
\033[1;30;47m[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\n\033[m''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f'O preço total do seu produto é \033[4;32;40m{total}R$\033[m')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f'O preço total do seu produto é \033[4;32;40m{total:.2f}R$\033[m')
elif opcao == 3:
    total = preco
    print(f'O preço total do seu produto é \033[4;32;40m{total:.2f}R$\033[m')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    print(f'O preço total do seu produto é \033[4;32;40m{total:.2f}R$\033[m')
else:
    print('\033[1:31mOpção inválida. Por favor, digite novamente.\033[m')