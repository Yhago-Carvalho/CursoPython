def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: Onúmero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial do número n.
    """
    fat = 1
    for i in range(n, 0, -1):
        if show:
            if i > 1:
                print(i, end=' x ')
            else:
                print(i, end=' = ')
        fat *= i
    return fat


print(fatorial(5, True))