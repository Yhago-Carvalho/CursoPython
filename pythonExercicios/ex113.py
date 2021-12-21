def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[31mO USUÁRIO PREFERIU NÃO DIGITAR ALGUM VALOR!\033[m')
            return 0
        except:
            print('\033[31mERRO, DIGITE UM NÚMERO INTEIRO VÁLIDO!\033[m')
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            r = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[31mO USUÁRIO PREFERIU NÃO DIGITAR ALGUM VALOR!\033[m')
            return 0
        except:
            print('\033[31mERRO, DIGITE UM NÚMERO REAL VÁLIDO!\033[m')
        else:
            return r


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaReal('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')
