dados = {}
dados['Nome'] = input('Nome: ')
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))
print(f'O nome é igual a {dados["Nome"]}')
print(f'A média é igual a {dados["Média"]}')
if dados['Média'] >= 7:
    print('APROVADO!!!!')
else:
    print('REPROVADO!!!')