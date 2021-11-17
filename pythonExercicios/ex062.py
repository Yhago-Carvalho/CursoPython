t1 = 0
t2 = 1
cont = 3
quant = int(input('Quantos termos da série Fibonacci deseja ver? '))
print(f'{t1} -> {t2} -> ', end='')
while cont <= quant:
    t1 += t2
    print(f'{t1} -> ', end='')
    aux = t1
    t1 = t2
    t2 = aux
    cont += 1
print('ACABOU')