from datetime import date
cont = 0
ano_atual = date.today().year
for c in range(1, 8):
    ano_nasc = int(input(f'Qual ano de nascimento da {c}ª pessoa? '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        cont += 1
print(f'{cont} pessoas já atingiram a maioridade e {7 - cont} ainda não')
