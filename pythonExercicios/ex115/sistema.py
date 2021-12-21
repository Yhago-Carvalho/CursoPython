from lib.arquivo import *
from lib.interface import *


if not arquivo_existe('cursoemvideo.txt'):
    criar_arquivo('cursoemvideo.txt')
while True:
    o = menu('Sua opção: ')
    if o == 1:
        #Mostra as pessoas cadastradas
        ler_arquivo('cursoemvideo.txt')
    elif o == 2:
        #Cadastra uma pessoa
        titulo('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar('cursoemvideo.txt', nome, idade)
    else:
        #Sai do sistema
        titulo('SISTEMA FINALIZADO... ATÉ LOGO!')
        break