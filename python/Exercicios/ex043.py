# CALCULADORA DE IMC

peso = float(input('Informe seu peso (KG): '))
altura = float(input('Informe sua altura (M): '))

imc = peso / (altura * altura)

print(f'Seu imc é {imc:.2f}')

if imc < 18.5:
    print('Você está classificado (a) como uma pessoa \033[1:34mAbaixo do Peso\033[m.')
elif imc < 25.00:
    print('Você está classificado (a) como uma pessoa que está no \033[1:32mPeso Ideal\033[m.')
elif imc < 30.00:
    print('Você está classificado (a) como uma pessoa que está com \033[1:33mSobrepeso.')
elif imc < 40.00:
    print('Você está classificado (a) como uma pessoa com \033[1:35mObesidade\033[m.')
else:
    print('Você está classificado (a) como uma pessoa com \033[1:31mObesidade Mórbida\033[m.')


# EXERCICIO FEITO PELO PROFESSOR

'''peso = float(input('Qual é o seu peso (Kg)? '))
altura = float(input('Qual é a sua altura(m)? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('Você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA.')'''




















