nome = input('Digite seu nome completo: ')
print(f'Seu nome com todas letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas é: {nome.lower()}')
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras')
nome1 = nome.split()
print(f'Seu primero nome tem {len(nome1[0])} letras')