from time import sleep
from random import randint
from operator import itemgetter
resultado = {
    'Jogador 1':randint(1, 6),
    'Jogador 2':randint(1, 6),
    'Jogador 3':randint(1, 6),
    'Jogador 4':randint(1, 6)}
classificação = []
print('Valores sorteados:')
for j, r in resultado.items():
    print(f'O {j} tirou {r}')
    sleep(1)
classificação = sorted(resultado.items(), key=itemgetter(1), reverse=True)
print('>>>>> RESULTADO <<<<<')
for j, r in enumerate(classificação):
    print(f'O {j+1}º lugar: {r[0]} tirou {r[1]}')
    sleep(1)
