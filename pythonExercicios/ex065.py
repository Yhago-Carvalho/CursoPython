soma = maior = menor = cont = 1
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    if cont == 1:
        menor = maior = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
    cont += 1
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite uma opção válida [S/N]: ')).strip().upper()[0]
print(f'A média dos números digitados é {soma/cont:.2f}, o menor número foi {menor} e o maior foi {maior}')