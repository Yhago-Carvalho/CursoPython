import math
oposto = float(input('Qual comprimento do cateto oposto? '))
adjacente = float(input('Qual comprimento do cateto adjacente? '))
h = math.hypot(oposto, adjacente)
print(f'O comprimento da hipotenusa é {h:.2f}')
