# DANDO AUMENTO PARA UM FUNCIONARIO

nomeqra = input('Digite o nome de para quem você vai dar um aumento:')
salb = float(input('Qual o sálario atual dessa pessoa?:'))
aumento = float(input('Digite a porcentagem do aumento a ser concedido:'))
aumentod = aumento / 100
salca = salb * aumentod
nsal = salca + salb
print(f'O salário do(a) {nomeqra} era de {salb:.2f}R$, mas, devido ao aumento de {aumento:.0f}%, '
      f'seu novo sálario será {nsal:.2f}R$.')