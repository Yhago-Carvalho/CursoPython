números = []
for c in range(5):
    números.append(int(input(f'Digite um número para posição {c} da lista: ')))
print(f'A lista obtida foi {números}')
print(f'O maior número digitado foi {max(números)}, nas posições ', end='')
for p, n in enumerate(números):
    if n == max(números):
        print(f'{p}...', end=' ')
print(f'\nO menor número digitado foi {min(números)}, nas posições ', end='')
for p, n in enumerate(números):
    if n == min(números):
        print(f'{p}...', end=' ')
