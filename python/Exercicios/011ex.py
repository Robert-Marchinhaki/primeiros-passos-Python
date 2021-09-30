# CALCULANDO QUANTOS BALDES DE TINTA SERIA NECESSÁRIO PARA PINTAR UMA PAREDE

altura = float(input('Meça a altura da sua parede (metros):'))
largura = float(input('Meça a largura da sua parede (metros):'))
metroq = altura * largura
tintal = 1
tintap = 2
baldest = metroq / tintap
print(
    "A peça da sua casa em questão tem {:.2f}m2, sabendo que cada balde de tinta tem {:.2f}litro, então, vai ser necessário {:.2f} baldes"
    " de tinta "
    " para pintar tudo".format(metroq, tintal, baldest))
