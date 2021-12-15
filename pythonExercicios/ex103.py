def ficha(jogador, gols):
    if jogador.strip() == '':
        jogador = '<Desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
tot = str(input('Total de gols no campeonato: '))
print(ficha(nome, tot))
