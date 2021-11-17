soma = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c+1}º número: '))
    if n%2 == 0:
        soma += n
print(f'A soma dos números pares digitados é: {soma}')
