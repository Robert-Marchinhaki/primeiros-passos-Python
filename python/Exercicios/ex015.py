# CALCULANDO OS CUSTOS DE ALUGAR UM CARRO

diasal = float(input('Por quantos dias o carro foi alugado?'))
kmrod = float(input('Quantos Km foram rodados?'))
diaso = diasal * 60
combus = kmrod * 0.15
total = diaso + combus
print(f'O total a pagar é de {total:.2f}')