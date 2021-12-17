def aumentar(p, porc, form=False):
    """
    -> Função para aumentar o preço.
    :param p: preço do produto.
    :param porc: porcentagem de aumento.
    :param form: Diz se quer o valor de retorno formatado ou não.
    :return: Valor do produto aumentado na porcentagem informada.
    """
    p *= (1+porc/100)
    if form == True:
        return moeda(p)
    else:
        return p


def diminuir(p, porc, form=False):
    """
    -> Função para diminuir o preço.
    :param p: preço do produto.
    :param porc: porcentagem de desconto.
    :param form: Diz se quer o valor de retorno formatado ou não.
    :return: Valor do produto descontado na porcentagem informada.
    """
    p *= (1 - porc/100)
    if form == True:
        return moeda(p)
    else:
        return p


def metade(p, form=False):
    """
    -> Função para calcular a metada do valor de um produto.
    :param p: preço do produto.
    :param form: Diz se quer o valor de retorno formatado ou não.
    :return: Valor do produto descontado pela metade.
    """
    p = p/2
    if form == True:
        return moeda(p)
    else:
        return p


def dobro(p, form=False):
    """
    -> Função para calcular o dobro do valor de um produto.
    :param p: preço do produto.
    :param form: Diz se quer o valor de retorno formatado ou não.
    :return: Valor dobrado do produto.
    """
    p = p*2
    if form == True:
        return moeda(p)
    else:
        return p


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(p, a, r):
    """
    -> Função para trazer um resumo sobre preço do produto.
    :param p: preço do produto.
    :param a: porcentagem de aumento.
    :param r: porcentagem de redução.
    :return: Tabela com o resumo dos preços.
    """
    print('-'*36)
    print(f'{"RESUMO DO VALOR":^36}')
    print('-'*36)
    print(f'Preço analisado:    R${moeda(p)}')
    print(f'Dobro do preço:     R${dobro(p, True)}')
    print(f'Metade do preço:    R${metade(p, True)}')
    print(f'{a:<4.1f}% de aumento:   R${aumentar(p, a, True)}')
    print(f'{r:<4.1f}% de desconto:  R${diminuir(p, r, True)}')
    print('-'*36)

