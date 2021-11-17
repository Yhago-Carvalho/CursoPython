n = int(input('Digite um número inteiro: '))
op = int(input('''Em qual base desja ver o número transformado?
[1] Binário
[2] Octal
[3] Hexadecimal
Digite a opção desejada: '''))
if op == 1:
    print(f'O número {n} na base binária é: {bin(n)[2:]}')
elif op == 2:
    print(f'O número {n} na base octal é: {oct(n)[2:]}')
elif op == 3:
    print(f'O número {n} na base hexadecimal é: {hex(n)[2:]}')
else:
    print('Digite uma opção válida')
