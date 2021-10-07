# OBTENDO O VALOR DE SENO, COSSENO E TANGENTE

from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'\n O valor de seno é igual {seno:.2f}.'
      f'\n O valor de cosseno é igual a {cosseno:.2f}.'
      f'\n O valor da tangente é igual a {tangente:.2f}')