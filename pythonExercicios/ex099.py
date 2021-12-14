from time import sleep
def maior(*núm):
    print('Analisando os valores...')
    mai = 0
    for i in núm:
        print(i, end=' ')
        sleep(0.3)
        if mai == 0:
            mai = i
        else:
            if mai < i:
                mai = i
    print(f'\nForam informados {len(núm)} ao todo.')
    print(f'O maior valor informado foi {mai}.')
    print('-='*30)

maior(9, 5, 7, 4, 6, 8, 1, 3, 4)
maior(77, 5, 8, 74, 5, 8, 7, 2, 98, 52)
maior(1, 2)
maior(6)
maior()
