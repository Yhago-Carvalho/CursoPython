def leiaInt(msg):
    n = str(input(msg))
    while not n.isnumeric():
        print('\033[31mERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
        n = str(input('Digite um número: '))
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
