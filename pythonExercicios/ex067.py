cont = 0
while True:
    print('=-'*30)
    n = int(input('Digite o número que deseja ver a tabuada: '))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n:^3} x {cont:^3} = {cont*n:^3}')
        cont += 1
    cont = 0
