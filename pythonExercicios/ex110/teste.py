import moeda


preço = float(input('Qual preço do produto? R$'))
aumento = float(input('Qual taxa de aumento? '))
redução = float(input('Qual taxa de redução? '))
moeda.resumo(preço, aumento, redução)
