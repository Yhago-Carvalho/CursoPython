i = int(input('Qual a idade do atleta? '))
if i <= 9:
    print('\33[1;31mCATEGORIA MIRIM!')
elif i <= 14:
    print('\33[1;32mCATEGORIA INFALTIL!')
elif i <= 19:
    print('\33[1;33mCATEGORIA JÚNIOR!')
elif i == 20:
    print('\33[1;34mCATEGORIA SÊNIOR!')
else:
    print('\33[1;35mCATEGORIA MASTER!')
