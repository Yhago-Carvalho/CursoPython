from datetime import date
nas = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - nas
print(f'Quem nasceu em {nas} tem {idade} anos em {atual}')
if idade < 18:
    print(f'Ainda não está na hora de se alistar, faltam {18 - idade} anos, deverá se alistar no ano de {nas + 18}')
elif idade > 18:
    print(f'Já passou {idade - 18} anos da hora de se alistar, deveria ter se alistado em {nas + 18}')
else:
    print('Precisa se alistar IMEDIATAMENTE!')
