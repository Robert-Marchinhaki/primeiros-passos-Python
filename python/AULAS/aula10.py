# nome = str(input('Qual é seu nome? '))
# if nome == 'Robert':
#    print('Que nome lindo você tem!')
# else:
#    print('Seu nome tão comum!')
# print(f'Bom dia, {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:.1f}')
if m < 6.0:
    print('Você está abaixo da média.')
else:
    print('Parabéns! Você atingiu a média.')

