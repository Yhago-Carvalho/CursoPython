tot_gasto = mais_1000 = mais_barato = 0
continuar = 'S'
while continuar in 'Ss':
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$'))
    print('-'*30)
    tot_gasto += preço
    if preço > 1000:
        mais_1000 =+ 1
    if mais_barato == 0:
        mais_barato = preço
        produto_mais_barato = produto
    elif mais_barato > preço:
        mais_barato = preço
        produto_mais_barato = produto
    continuar = str(input('Deseja continuar [S/N]?'))
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar [S/N]?'))
print(f'''O total gasto nas compras foi de R${tot_gasto:,.2f}
Foi comprado {mais_1000} produtos por mais de 1000 reais
O produto mais barato foi {produto_mais_barato}''')
