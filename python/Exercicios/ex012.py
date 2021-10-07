# DANDO DESCONTOS EM PRODUTOS

preçop = float(input('Qual o preço do produto?'))
desconto = float(input('Quantos porcento de desconto vão ser dados?'))
despor = desconto / 100
valord = preçop * despor
preçocd = preçop - valord
print(
    'O preço do produto sem desconto é de {:.3f}. Mas, se o pagamento for á vista, '
    'você receberá um desconto de {:.1f}% e o preço do produto vai cair para {:.3f}R$'.format(preçop, desconto, preçocd))
