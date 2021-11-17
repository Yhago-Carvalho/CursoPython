nome = str(input('Digite seu nome completo: ')).strip()
nomel = nome.split()
print(f'Seu primeiro nome é: {nomel[0]}')
print(f'Seu último nome é: {nomel[len(nomel)-1]}')
