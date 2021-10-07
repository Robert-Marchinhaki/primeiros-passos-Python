# se for - 200Km vai custar 0,50 por Km
# se for + 200Km vai custar 0,45 por Km

# DANDO DESCONTO EM UMA VIAGEM DE ACORDO COM A QUANTIDADE DE Km

dist = float(input('Digite quantos Km vai ter sua viagem: '))
if dist <= 200:
    print(f'Sua viagem vai custar {0.50*dist:.2f}R$')
else:
    print(f'Sua viagem vai custar {0.45*dist:.2f}R$.')

# EXERCICIO FEITO PELO PROFESSOR
# distancia = float(input('Qual é a distância da viagem? '))
# print(f'Você está prestes a começar uma viagem de {distancia}Km.')
# ''' preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45 '''
# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45
# print(f'O preço da sua passagem vai ser de {preco:.2f}R$')