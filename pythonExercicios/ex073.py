times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza','Corinthians', 'Bragantino', 'Internacional',
         'Fluminense', 'América-MG', 'Ceará', 'Santos', 'Cuiabá', 'Atlético-PR', 'Juventude', 'Atlético-GO',
         'São Paulo', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense')
print('-'*20)
print('Os 5 primeiros colcoados são:')
for  pos in range(0, 5):
    print(f'{pos +1}º {times[pos]}')
print('-'*20)
print('Os 4 últimos colcoados são:')
for  pos in range(16, 20):
    print(f'{pos + 1}º {times[pos]}')
print('-'*20)
print(sorted(times))
print('-'*20)
print(f'A chapeconse se encontra na {times.index("Chapecoense")+1}º posição')
