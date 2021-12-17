def aumentar(p, porc):
    """
    -> Função para aumentar o preço.
    :param p: preço do produto.
    :param porc: porcentagem de aumento.
    :return: Valor do produto aumentado na porcentagem informada.
    """
    p *= (1+porc/100)
    return p


def diminuir(p, porc):
    """
    -> Função para diminuir o preço.
    :param p: preço do produto.
    :param porc: porcentagem de desconto.
    :return: Valor do produto descontado na porcentagem informada.
    """
    p *= (1 - porc/100)
    return p


def metade(p):
    """
    -> Função para calcular a metada do valor de um produto.
    :param p: preço do produto.
    :return: Valor do produto descontado pela metade.
    """
    p = p/2
    return p


def dobro(p):
    """
    -> Função para calcular o dobro do valor de um produto.
    :param p: preço do produto.
    :return: Valor dobrado do produto.
    """
    p = p*2
    return p