s = float(input('Qual valor do seu salário? R$'))
if s > 1250.0:
    print(f'Seu aumento foi de 10%, logo seu salário ficará R${s * 1.1}')
else:
    print(f'Seu aumento foi de 15%, logo seu salário ficará R${s * 1.15}')
