import moeda


p = float(input('Digite o valor do produto: R$'))
acrescimo = float(input('Qual porcentagem você quer ver acrescida no produto? '))
desconto = float(input('Qual porcentagem você quer ver descontada no produto? '))
print('-'*50)
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando {acrescimo}%, {moeda.aumentar(p, acrescimo, True)}')
print(f'Descontando {desconto}%, {moeda.diminuir(p, desconto, True)}')
