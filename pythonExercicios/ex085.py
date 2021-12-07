números = [[],[]]
for i in range(7):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if n % 2 == 0:
        números[0].append(n)
    else:
        números[1].append(n)
print(f'Os valores pares digitados foram {sorted(números[0])}')
print(f'Os valores ímpares digitados foram {sorted(números[1])}')
