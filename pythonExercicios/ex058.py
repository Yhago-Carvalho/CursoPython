from random import randint
print('='*31)
print('      JOGO DA ADIVINHAÇÃO')
print('='*31)
palpites = c = 0
n = 1
c = randint(0, 10)
while n!=c:
    n = int(input('Digite um valor entre 0 e 10: '))
    while n<0 or n>10:
        n = int(input('Digite um valor válido: '))
    if n <= c:
        print('Mais... Tente mais uma vez!')
    elif n >= c:
        print('Menos... Tente mais uma vez!')
    palpites += 1
print(f'PARABÉNS, você acertou. \nForam necessárias {palpites} tentativas.')
