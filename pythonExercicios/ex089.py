lista = []
aluno = []
notas = []
resp = 'S'
while resp in 'Ss':
    aluno.append(input('Nome: '))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    aluno.append(notas[:])
    lista.append(aluno[:])
    notas.clear()
    aluno.clear()
    resp = input('Deseja continuar [S/N]? ').strip()[0]
print('-='*22)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":^5}')
print('-'*30)
for i in range(len(lista)):
    print(f'{i+1:<5}{lista[i][0]:<10}{(lista[i][1][0] + lista[i][1][1])/2:^5.1f}')
print('-'*30)
n = 0
while n != 999:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if n == 999:
        break
    print(f'Notas de {lista[n-1][0]} são {lista[n-1][1]}')
    print('-' * 30)
print('FINALIZANDO...')
print('>>> VOLTE SEMPRE <<<')