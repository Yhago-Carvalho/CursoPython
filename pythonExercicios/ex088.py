from random import randint
from time import sleep

print('-'*40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-'*40)
jogos = []
jogo = []
quant = int(input('Quantos jogos você quer sortear? '))

for i in range(quant):
    for j in range(6):
        n = randint(1, 60)
        while n in jogo:
            n = randint(1, 60)
        jogo.append(n)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()

print(f'-=-=-= SORTEANDO {quant} JOGOS -=-=-=')
for i in range(quant):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(0.75)
print('-=-=-=- < BOA SORTE > -=-=-=-')
