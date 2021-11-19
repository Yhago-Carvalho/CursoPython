cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = 's'
while continuar not in 'Nn':
    n = int(input('Digite um número entre 0 e 20: '))
    while 0 > n or n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {cont[n]}')
    continuar = input('Deseja continuar [S/N]? ')
