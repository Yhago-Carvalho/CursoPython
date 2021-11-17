print('=-'*29)
print('                   CADASTRO DE PESSOAS')
print('=-'*29)
mais_18 = homens = mulheres_menos_20 = 0
continuar = 'S'
while continuar in 'Ss':
    pessoa = str(input('Nome: '))
    sexo = str(input('Sexo [M/F]: '))
    while sexo not in 'FfMm':
        sexo = str(input('Sexo [M/F]: '))
    idade = int(input('Idade: '))
    print('-'*20)
    if idade > 18:
        mais_18 += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres_menos_20 += 1
    continuar = str(input('Deseja coninuar[S/N]? '))
    while continuar not in 'SsNn':
        continuar = str(input('Digite uma opção válida [S/N]: '))
    print('-' * 20)
print(f'Foram cadastradas {mais_18} pessoas com mais de 18 anos, {homens} homens e {mulheres_menos_20} mulheres com menos de 20 anos')