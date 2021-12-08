dados = {}
gols = []
dados['Jogador'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols {dados["Jogador"]} fez na partida {i+1}? ')))
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)
print('-='*40)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*40)
print(f'O jogador {dados["Jogador"]} jogou {partidas} partidas.')
for i in range(partidas):
    print(f'    => Na partida {i+1}, fez {dados["Gols"][i]} gol(s).')
print(f'Fez um total de {dados["Total"]} gols.')
