import moeda

p = float(input('Digite o valor do produto: R$'))
acrescimo = float(input('Qual porcentagem você quer ver acrescida no produto? '))
desconto = float(input('Qual porcentagem você quer ver descontada no produto? '))
print('-'*50)
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando {acrescimo}%, R${moeda.aumentar(p, acrescimo)}')
print(f'Descontando {desconto}%, R${moeda.diminuir(p, desconto)}')
