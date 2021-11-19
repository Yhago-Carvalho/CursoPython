num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))

print(f'Os valores digitados foram: {num}')
print(f'O valor 9 foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print('O valores pares digitados foram: ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
