def voto(ano_nasc):
    from datetime import date
    idade = date.today().year - ano_nasc
    if 65 >= idade >= 18:
        return f'Com {idade} anos: Voto Obrigatório.'
    elif idade >= 16 or idade > 65:
        return f'Com {idade} anos: Voto Opcional.'
    else:
        return f'Com {idade} anos: Voto Negado.'


print('-'*30)
ano = int(input('Ano de nascimento: '))
print(voto(ano))
