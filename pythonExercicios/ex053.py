f = input('Digite uma frase: ').lower().replace(' ', '')
cont = 0
i = 0
for c in range(len(f), 0, -1):
    if f[i] == f[c-1]:
        cont += 1
    i += 1
if cont == len(f):
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')
