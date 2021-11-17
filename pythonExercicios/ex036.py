casa = float(input('Qual valor da casa? R$'))
s = float(input('Qual valor do seu salário? R$'))
a = int(input('Em quantos anos deseja pagar a casa?'))

parcela = casa / (a * 12)
if parcela <= 0.3 * s:
    print(f'Parabéns, você está apto para compra da casa, vamos fechar negócio! \nVocê pagará em {a*12} parcelas de {parcela:.2f}')
else:
    print(f'Que pena, a parcela de R${parcela:.2f} é muito alta para seu salário, seria necessário um salário de R${parcela/0.3:.2f}')
