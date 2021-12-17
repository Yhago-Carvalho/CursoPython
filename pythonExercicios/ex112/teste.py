from utilidadescev import moeda
from utilidadescev import dados


valor = dados.leiaDinheiro('Qual preço do produto? R$')
moeda.resumo(valor, 5, 30)
