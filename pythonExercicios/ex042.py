print('-=-' * 20)
print('                ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)
r1 = int(input('Digite o comprimeto da reta 1: '))
r2 = int(input('Digite o comprimeto da reta 2: '))
r3 = int(input('Digite o comprimeto da reta 3: '))
if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Com esses valores não conseguimos formar um triângulo!')
else:
    print('Ótimo, conseguimos formar um triângulo')
    if r1 == r2 == r3:
        print('E este é um triângulo equilátero.')
    elif r1 != r2 != r3 != r1:
        print('E este é um triângulo escaleno.')
    else:
        print('E este é um triângulo isóceles.')
