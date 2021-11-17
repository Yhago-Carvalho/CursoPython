h_velho = 0
cont_mulher = 0
soma = 0
for c in range(0, 4):
    print(f'------{c+1}ª PESSOA------')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').lower()
    soma += idade
    if sexo == 'm' and idade > h_velho:
        mais_velho = nome
        h_velho = idade
    if sexo == 'f' and idade < 20:
        cont_mulher += 1
print('-'*30)
print(f'A média de idade é de {soma/4} anos')
if h_velho == 0:
    print(f'não há homens na lista')
else:
    print(f'O homem mais velho é {mais_velho}, com idade de {h_velho} anos')
if cont_mulher == 0:
    print('Não há mulheres com menos de 20 anos')
else:
    print(f'Há {cont_mulher} mulher(es) com menos de 20 anos')
print('-'*30)
