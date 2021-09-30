# OBTENDO O VALOR DA HIPOTENUSA

from math import hypot
catopo = float(input('Digite o comprimento do cateto oposto:'))
catadj = float(input('Digite o comprimento do cateto adjacente:'))
hipotenusa = hypot(catopo, catadj)
print(f'O valor da hipotenusa desse triângulo retângulo é {hipotenusa:.2f}')