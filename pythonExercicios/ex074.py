from random import randint
números = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end = '')
for n in números:
    print(n, end = ' ')
print(f'\nO maior número é {max(números)}')
print(f'O menor número é {min(números)}')