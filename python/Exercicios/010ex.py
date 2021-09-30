# CALCULANDO QUANTOS DOLARS VOCÊ PODERIA OBTER NA COTAÇÃO DE 5,15$

cart = float(input('Quantos de dinheiro você tem atualmente?'))
dolar = 5.15
convert = cart / dolar
print('Você tem {:.2f}R$ que pode ser convertido para {:.2f}$ dólar(es)'.format(cart, convert))
