'''nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Robert' or nome == 'Marco':
    print('Seu nome é maravilhoso! Parabéns.')
elif nome in ('Kiane Karon'):
    print('É um belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')'''

from random import choice
from time import sleep
print('Vamos brincar de pedra, papel ou tesoura. Tente me vencer.')
print('pedra, papel, tesoura...')
sleep(3)
player1 = str(input('O que você escolheu? '))
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
print(f'Eu escolhi {computador}.')
if player1 == 'tesoura' and computador == 'papel':
    print('Você me venceu!')
elif player1 == 'tesoura' and computador == 'tesoura':
    print('Empatamos! A gente escolha a mesma coisa.')
elif player1 == 'tesoura' and computador == 'pedra':
    print('HAHA, eu venci!')
elif player1 == 'papel' and computador == 'papel':
    print('Empatamos! A gente escolheu a mesma coisa.')
elif player1 == 'papel' and computador == 'pedra':
    print('Você me venceu!')
elif player1 == 'papel' and computador == 'tesoura':
    print('HAHA, eu venci!')
elif player1 == 'pedra' and computador == 'pedra':
    print('Empatamos! A gente escolheu a mesma coisa.')
elif player1 == 'pedra' and computador == 'tesoura':
    print('Você me venceu!')
elif player1 == 'pedra' and computador == 'papel':
    print('HAHA, eu venci!')
else:
    print('ERROR')
    print('Verefique se o que você escreveu está dentro das possibilidades')