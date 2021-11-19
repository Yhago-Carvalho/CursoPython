dados = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.90)
print('-'*50)
print(f'{"LISTAGEM DE PREÇO":^50}')
print('-'*50)
for c in range(0, len(dados), 2):
    print(f'{dados[c]:.<30} R$ {dados[c+1]:>7.2f}')
print('-'*50)
