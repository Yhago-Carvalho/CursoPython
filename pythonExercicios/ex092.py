from datetime import datetime as dt
dados = {}
dados['Nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
novos_dados = {
    'Idade': dt.now().year - nasc,
    'Carteira de trabalho': int(input('Carteira de trabalho (0 não tem):'))}
dados.update(novos_dados)
if dados['Carteira de trabalho'] > 0:
    novos_dados = {
        'Ano de contratação': int(input('Ano de contratação: ')),
        'Salário': float(input('Salário: '))}
    dados.update(novos_dados)
    dados['Idade de aposentadoria'] = 35 + dados['Ano de contratação'] - nasc
print('-='*30)
for k, i in dados.items():
    print(f'{k} tem o valor de {i}')
