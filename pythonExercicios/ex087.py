coluna3 = pares = maior2l = 0
matriz = []
linha = []
for i in range(3):
    for j in range(3):
        n = int(input(f'Digite o valor para posição [{i}][{j}]: '))
        linha.append(n)
    matriz.append(linha[:])
    linha.clear()
print('-='*25)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if j == 2:
            coluna3 += matriz[i][j]
    print()
print('-=' * 25)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da 3ª coluna é {coluna3}.')
print(f'O maior valor da 2ª linha é {max(matriz[1])}.')
