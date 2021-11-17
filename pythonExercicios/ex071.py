print('='*39)
print('              BANCO CEV')
print('='*39)
valor = int(input('Qual valor deseja sacar? R$'))
if valor // 100 > 0:
        print(f'Total de {valor // 100} cédulas de R$100,00')
        valor = valor % 100
if valor // 50 > 0:
        print(f'Total de {valor // 50} cédulas de R$50,00')
        valor = valor % 50
if valor // 20 > 0:
        print(f'Total de {valor // 20} cédulas de R$20,00')
        valor = valor % 20
if valor // 10 > 0:
        print(f'Total de {valor // 10} cédulas de R$10,00')
        valor = valor % 10
if valor // 5 > 0:
        print(f'Total de {valor // 5} cédulas de R$5,00')
        valor = valor % 5
if valor // 2 > 0:
        print(f'Total de {valor // 2} cédulas de R$2,00')
        valor = valor % 2
if valor == 1:
        print('Total de 1 cédulas de R$1,00')
