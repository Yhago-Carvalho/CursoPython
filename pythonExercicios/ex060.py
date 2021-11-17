n = int(input('Digite um número para saber seu fatorial: '))
fat = 1
while n!=0:
    fat *= n
    print(f'{n}', end = '')
    print(' = ' if n==1 else ' x ', end = '')
    n -= 1
print(fat)