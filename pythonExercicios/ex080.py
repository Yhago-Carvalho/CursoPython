lista = []
for c in range(5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        p = 0
        while p < len(lista):
            if num <= lista[p]:
                lista.insert(p, num)
                print(f'Adicionado na posição {p} da lista...')
                break
            p += 1
print('-='*25)
print(f'Os números adicionados foram {lista}')
