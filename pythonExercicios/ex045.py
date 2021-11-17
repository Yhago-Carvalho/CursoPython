from time import sleep
from random import randint
print('\33[1;36m=\33[m' * 40)
print('                \33[4;31mJOKENPÔ\33[m')
print('\33[1;36m=\33[m' * 40)
n = int(input('''[1] PEDRA
[2] PAPEL
[3] TESOURA
Digite a opção desejada: '''))
pc = randint(1, 3)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
if n > 3 or n < 1:
    print('Digite uma opção válida!')
elif n == pc:
    resultado = '\33[4mEMPATE\33[m'
    print('JO', end = '')
    sleep(0.5)
    print('KEN', end = '')
    sleep(0.5)
    print('PÔ!!!')
    print(f'O computador escolheu {itens[pc - 1]}, e o jogador escolheu {itens[n - 1]}:')
    print(f'{resultado}')
else:
    if n == 1 and pc == 3:
        resultado = '\33[4;32mVOCÊ GANHOU!\33[m'
    elif n == 2 and pc == 1:
        resultado = '\33[4;32mVOCÊ GANHOU!\33[m'
    elif n == 3 and pc == 2:
        resultado = '\33[4;32mVOCÊ GANHOU!\33[m'
    else:
        resultado = '\33[4;31mVOCÊ PERDEU!\33[m'
    print('JO', end = '')
    sleep(0.5)
    print('KEN', end = '')
    sleep(0.5)
    print('PÔ!!!')
    print(f'O computador escolheu {itens[pc - 1]}, e o jogador escolheu {itens[n - 1]}:')
    print(f'{resultado}')
