palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end = ' ')
    for v in range(0, len(c)):
        if c[v].lower() in 'aeiou':
            print(c[v], end = ' ')
