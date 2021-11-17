v = int(input('Qual a velocidade do carro no radar? '))
if v > 80:
    print(f'Você está acima da velocidade e vai ser multado em R${(v - 80)*7:.2f}')
print('Dirija com segurança, tenha um bom dia!')
