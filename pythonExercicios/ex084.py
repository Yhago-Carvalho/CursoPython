galera = []
pessoa = []
maior = menor = 0
resp = 'S'
while resp in 'Ss':
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if maior == menor == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    resp = input('Deseja continuar [S/N]? ').strip()[0]
print('-='*25)
print(f'Ao todo foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi de {maior} Kg. Peso de ', end='')
for i in galera:
    if i[1] == maior:
        print(f'[{i[0]}]', end=' ')
print(f'\nO menor peso foi de {menor} Kg. Peso de ', end='')
for i in galera:
    if i[1] == menor:
        print(f'[{i[0]}]', end=' ')
