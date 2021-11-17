sexo = str(input('Qual sexo da pessoa [M/F]? ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite uma opção válida [M/F]: ')).upper().strip()[0]
print(f'Sexo {sexo} informado com sucesso')