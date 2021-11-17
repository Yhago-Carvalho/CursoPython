dist = int(input('Qual a distância da sua viagem? '))
preço = dist * 0.5 if dist <= 200 else dist * 0.45
print(f'O preço da sua passagem é de R${preço:.2f}')
