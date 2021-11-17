print('='*30)
print('      ANALISANDO VALORES')
print('='*30)
op = 0
while op!= 5:
    n1 = float(input('Digite o 1º valor: '))
    n2 = float(input('Digite o 2º valor: '))
    op = int(input('''[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR \nOpção desejada: '''))
    if op == 4:
        while op == 4:
            n1 = float(input('Digite o 1º valor: '))
            n2 = float(input('Digite o 2º valor: '))
            op = int(input('Escolha uma nova opção'))
            print('')
    while op < 1 or op > 5:
        op = int(input('Escolha uma opção válida: '))
    if op == 1:
        print(f'A soma entre os valores {n1} e {n2} é {n1+n2}')
    if op == 2:
        print(f'A multiplicação entre os valores {n1} e {n2} é {n1 * n2}')
    if op == 3:
        if n1 == n2:
            print('Os números digitados são iguais')
        else:
            if n1 > n2:
                print(f'O número maior é {n1}')
            else:
                print(f'O número maior é {n2}')
    print('')
