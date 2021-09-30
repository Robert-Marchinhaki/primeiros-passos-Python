# MULTANDO UMA PESSOA DE ACORDO COM A VELOCIDADE QUE ELA PERCORRE

vel = int(input('Digite a velocidade do carro: '))
vel1 = 80 - vel
if vel > 80:
    print(f'Sua velocidade atual é {vel}Km/h, Você foi multado!')
    print(f'O valor da sua multa é de: {-7 * vel1}R$')

#   EXERCICIO FEITO PELO PROFESSOR

# velocidade = float(input('Digite a velocidade atual do carro: '))
# if velocidade > 80:
#     print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
#     multa = (velocidade - 80) * 7
#     print(f'Você deve pagar uma multa de {multa:.2f}')
# print('Tenha um bom dia! Dirija com segurança!')
