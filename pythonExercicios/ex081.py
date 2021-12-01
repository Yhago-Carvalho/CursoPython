lista = []
continuar = 's'
while continuar in 'Ss':
    lista.append(int(input('Digite um valor: ')))
    continuar = input('Deseja continuar [S/N]? ')[0].strip()
print(f'Você digitou {len(lista)} elementos')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse = True)}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
