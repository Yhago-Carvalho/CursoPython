frase = str(input('Escreva algo: ')).strip().upper()
print(f'A letra "a" aparece {frase.count("A")} vezes')
print(f'Aparece pela 1ª vez na posição {frase.find("A") + 1}')
print(f'Aparece pela última vez na posição {frase.rfind("A") + 1}')
