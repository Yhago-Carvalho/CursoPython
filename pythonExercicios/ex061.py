a1 = int(input('Digite o primeiro termo da P.A.: '))
r = int(input('Digite a razão para P.A.: '))
cont = 1
continuar = 'S'

while continuar == 'S':
    termos = int(input('Quantos termos da P.A. você deseja adicionar? '))
    while cont <= termos:
        if cont < termos:
            print(f'{a1}', end=' -> ')
        else:
            print(f'{a1}')
        a1 += r
        cont += 1
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite uma opção válida [S/N]: ')).upper().strip()
    cont = 1
