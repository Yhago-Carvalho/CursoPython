from utilidadescev import moeda
from utilidadescev import dados


p = dados.leiaDinheiro('Qual preço do produto? R$')
moeda.resumo(p, 5, 10)
