n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o vaçpr da segunda nota: '))
m = (n1 + n2)/2
if m >= 7:
    print(f'Sua média foi {m:.1f}, Parabéns você está aprovado!')
elif m < 5:
    print(f'Sua média foi {m:.1f}, você está reprovado!')
else:
    print(f'Sua média foi {m:.1f}, você está em recuperação!')
