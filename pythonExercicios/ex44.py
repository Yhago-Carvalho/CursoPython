print(f'{"LOJA CARVALHO":=^40}')
p = float(input('Qual preço do produto? R$'))
pag = int(input('''Escolha a forma de pagamento:
[1] À vista (dinheiro/cheque), com 10% de desconto;
[2] Débito, com 5% de desconto;
[3] Parcelado em 2x s/ júros;
[4] Parcelado em 3x ou mais com acréscimo de 20% de júros
Digite a opção desejada: '''))
if pag == 1:
    print(f'O produto sairá por R${p * 0.9:.2f}')
elif pag == 2:
    print(f'O produto sairá por R${p * 0.95:.2f}')
elif pag == 3:
    print(f'O produto sairá por R${p:.2f}')
elif pag == 4:
    print(f'O produto sairá por R${p * 1.2:.2f}')
else:
    print('Opção inváida!')
