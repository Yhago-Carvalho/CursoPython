matriz = []
linha = []
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite um número para posição [{i}][{j}]: '))
        linha.append(n)
    matriz.append(linha[:])
    linha.clear()
print('-='*20)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
    print()
