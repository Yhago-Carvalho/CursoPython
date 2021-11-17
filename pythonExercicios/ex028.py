from random import randint
from time import sleep
nc = int(randint(0, 5))
nu = int(input('Qual número entre 0 e 5 você acha que foi sorteado? '))
print('PROCESSANDO...')
sleep(2)
if nc == nu:
    print(f'O número sorteado foi {nc}, Parabéns, você acertou')
else:
    print(f'O número sorteado foi {nc}, tente outra vez!')
