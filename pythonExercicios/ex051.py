a1 = int(input('Qual 1º termo da P.A.? '))
r = int(input('Qual a razão da P.A.? '))
for c in range(a1, a1 + 10*r, r):
    print(f'{c}', end = ' -> ')
print('Acabou')
