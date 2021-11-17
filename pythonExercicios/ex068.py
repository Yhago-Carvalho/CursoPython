from random import randint
cont = 0
while True:
    jogador = str(input('PAR OU ÍMPAR? ')).strip().upper()
    while jogador != 'PAR' and jogador != 'ÍMPAR':
        jogador = str(input('Digite uma opção válida [PAR/ÍMPAR]: ')).strip().upper()
    jogada = int(input('Qual número deseja jogar? '))
    computador = randint(0, 10)
    if jogador == 'PAR' and (jogada + computador)%2 == 1:
        break
    elif jogador == 'ÍMPAR' and (jogada + computador)%2 == 0:
        break
    if (jogada + computador)%2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você escolheu {jogador}, jogou {jogada}, o computador jogou {computador} e o resultado foi {resultado}, VOCÊ VENCEU!')
    cont += 1
print(f'Você escolheu {jogador}, jogou {jogada}, o computador jogou {computador} e o resultado foi {resultado}, VOCÊ PERDEU!')
print(f'Você venceu {cont} vezes consecutivas')
