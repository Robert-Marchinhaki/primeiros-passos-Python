# VERIFICADOR DE NATAÇÃO

from datetime import date
nascimento = int(input('Digite se ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
print(f'O atleta tem {idade} anos')

if nascimento > anoatual:
    print('Por favor, verefique se a data digitada é inferior ao ano atual.')
elif idade <= 9:
    print('De acordo com sua idade, você entraria na categoria \033[1:36mMIRIM\033[m.')
elif idade <= 14:
    print('De acordo com sua idade, você entraria na categoria \033[1:34mINFANTIL\033[m.')
elif idade <= 19:
    print('De acordo com sua idade você entraria na categoria \033[1:35mJUNIOR\033[m.')
elif idade == 20:
    print('De acordo com sua idade você entraria na categoria \033[1:97mSÊNIOR\033[m.')
else:
    print('De acordo com sua idade você entraria na categoria \033[1:30:44mMASTER\033[m.')

# EXERCICIO FEITO PELO PROFESSOR

'''from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')'''