números = []
continuar = 's'
while continuar in 'Ss':
    n = int(input('Digite um valor: '))
    if n in números:
        print('Número duplicado! Não será adiconado.')
    else:
        números.append(n)
        print('Número adicionado com sucesso!')
    continuar = input('Deseja continuar? [S/N] ')[0].strip().upper()
print('-='*25)
print(f'Você digitou os valores {sorted(números)}')
