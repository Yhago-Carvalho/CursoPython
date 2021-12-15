def notas(*n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param n: Uma ou mais notas dos alunos.
    :param sit: (opcional) Indicando se mostra ou não a situação.
    :return: Dicionário com informações e situação da turma.
    """
    lista = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': float(f'{sum(n) / len(n):.2f}')
    }
    if sit:
        if lista['média'] >= 7:
            lista['situação'] = 'Boa'
        elif lista['média'] >= 5:
            lista['situação'] = 'Razoável'
        else:
            lista['situação'] = 'Ruim'
    return lista


print(notas(9.7, 8.3, 6, 5.2, sit=True))