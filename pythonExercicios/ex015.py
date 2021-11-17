dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram rodados? '))
valor = 60 * dias + 0.15 * km
print(f'O valor a se pagar pelo aluguel após {dias} e {km:.2f}km percorridos é de R${valor:.2f}')