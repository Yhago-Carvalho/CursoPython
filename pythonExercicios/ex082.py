lista = []
listaPar = []
listaImpar = []
continuar = 'S'
while continuar in 'Ss':
    lista.append(int(input('Digite um número: ')))
    continuar = input('Deseja continuar [S/N]? ').strip()[0]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        listaPar.append(lista[i])
    else:
        listaImpar.append(lista[i])
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {listaPar}')
print(f'A lista de números ímpares é {listaImpar}')
