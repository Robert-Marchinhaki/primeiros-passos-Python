expressao = str(input('Digite a expressão: '))
calculo = []
for simb in expressao:
    if simb == '(':
        calculo.append('(')
    elif simb == ')':
        if len(calculo) > 0:
            calculo.pop()
        else:
            calculo.append(')')
            break
if len(calculo) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')