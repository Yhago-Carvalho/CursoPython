dados = []
soma = 0
resp = 'S'
while resp in 'Ss':
    pessoa = {
        'Nome': input('Nome: '),
        'Sexo': input('Sexo [M/F]: '),
        'Idade': int(input('Idade: '))}
    dados.append(pessoa)
    resp = input('Deseja continuar? [S/N] ').strip()[0]
print('-='*30)
print(f'- O grupo tem {len(dados)} pessoas.')
for i in range(len(dados)):
    soma += dados[i]['Idade']
print(f'- A média de idade é de {soma/len(dados):.2f} anos.')
print('- As mulheres cadastradas foram: ',end='')
for i in range(len(dados)):
    if dados[i]['Sexo'] in 'Ff':
        print(dados[i]['Nome'], end=' ')
print('\n- Lista de pessoas que estão acima da média: ')
for i in dados:
    if i["Idade"] > soma/len(dados):
        print('   ', end='')
        for k, v in i.items():
            print(f'{k} = {v} ;', end='')
        print()
