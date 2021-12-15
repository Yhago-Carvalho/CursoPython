from time import sleep


def título(msg):
    print('\033[7;30;44m~' * (len(msg) + 4))
    print(f'\033[1;30;44m  {msg}')
    print('\033[7;30;44m~' * (len(msg) + 4))
    print('\033[m', end='')


def acessando(comando):
    texto = 'Acessando o manuel do comando '
    print('\033[1;36;40m~' * (len(texto) + len(comando) + 6))
    print(f"\033[1;36;40m  {texto}'{comando}'")
    print('\033[1;36;40m~' * (len(texto) + len(comando) + 6))


def manual(comando):
    print('\033[7;30;42m', end='')
    help(comando)


while True:
    título('SISTEMA DE AJUDA PyHELP')
    opc = input('Função ou Biblioteca -> ').strip().lower()
    if opc == 'fim':
        break
    sleep(0.5)
    acessando(opc)
    sleep(1)
    manual(opc)
    sleep(1)
título('ATÉ LOGO!')
