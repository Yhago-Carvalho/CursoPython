from math import trunc
n = int(input('Digite um número de 0 a 9999: '))
mil = trunc(n/1000)
cen = trunc((n - mil * 1000)/100)
dez = trunc((n - mil * 1000 - cen * 100)/10)
und = n - mil * 1000 - cen * 100 - dez * 10
print(f'Unidades: {und}')
print(f'Dezenas: {dez}')
print(f'Centenas: {cen}')
print(f'Milhar: {mil}')
