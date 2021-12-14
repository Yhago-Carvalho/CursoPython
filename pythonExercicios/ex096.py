def área(c, l):
    A = c*l
    print(f'A área de um terreno com dimensões {c:.2f}m x {l:.2f}m é {A:.2f}m')

print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
a = float(input('Comprimento (m): '))
b = float(input('Largura (m): '))
área(a, b)
