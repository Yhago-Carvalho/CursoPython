from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 25)
    if passo == 0:
        passo = 1
    passo = abs(passo)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}:')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.3)
        print('FIM!!!')
    elif inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
            sleep(0.3)
        print('FIM!!!')
    else:
        return print('Fim e início iguais, não há contagem!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
