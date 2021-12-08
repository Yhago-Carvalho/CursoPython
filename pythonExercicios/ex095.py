gols = []
dados = []
jogador = {}
soma = 0
resp = 's'
while resp in 'Ss':
    print('-' * 50)
    jogador['Nome'] = input('Nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
        soma += gols[i]
    jogador['Gols'] = gols[:]
    jogador['Total'] = soma
    soma = 0
    resp = input('Deseja continuar [S/N]? ').strip()[0]
    gols.clear()
    dados.append(jogador.copy())
print('-='*25)
print(f'{"cod":<5}{"Nome":<12}{"Gols":<12}{"Total":>7}')
print('-'*33)
for p, v in enumerate(dados):
    print(f'{p+1:^5}{v["Nome"]:<12}{str(v["Gols"]):<12}{v["Total"]:^7}')
while True:
    print('-' * 33)
    n = int(input('Mostrar dados de Qual jogador? (999 para encerrar)  '))
    if n == 999:
            break
    elif n <= 0 or n > len(dados):
        print(f'ERRO! Não existe jogador com código {n}, tente novamente')
    else:
        print(f'Levantametno do jogador {dados[n-1]["Nome"]}:')
        for p, v in enumerate(dados[n-1]['Gols']):
            print(f'Na partida {p+1} fez {v} gol(s).')
print('-' * 33)
print(f'{"VOLTE SEMPRE":*^20}')