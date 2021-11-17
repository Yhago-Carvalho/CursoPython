from datetime import date
a = int(input('Digite um ano para saber se ele é bissexto, caso queira o ano atual digite 0: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'Ano de {a} Bisexto')
else:
    print(f'O ano de {a} não é Bisexto!')
