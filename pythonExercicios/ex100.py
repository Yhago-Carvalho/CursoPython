from random import randint
from time import sleep


def sorteio(lista: list):
    print('Sorteando 5 valores da lista: ', end=' ')
    for n in range(5):
        lista.append(randint(1, 10))
        print(lista[n], end=' ')
        sleep(0.3)
    print('PRONTO!')

def SomaPar(lista: list):
    soma = 0
    for n in lista:
        if n%2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = []
sorteio(números)
SomaPar(números)
