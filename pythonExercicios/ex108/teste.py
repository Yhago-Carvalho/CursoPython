import moeda

p = float(input('Digite o valor do produto: R$'))
acrescimo = float(input('Qual porcentagem você quer ver acrescida no produto? '))
desconto = float(input('Qual porcentagem você quer ver descontada no produto? '))
print('-'*50)
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {acrescimo}%, {moeda.moeda(moeda.aumentar(p, acrescimo))}')
print(f'Descontando {desconto}%, {moeda.moeda(moeda.diminuir(p, desconto))}')
