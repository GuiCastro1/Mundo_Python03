'''
Criado por: Gui Castro

31/01/2025

Crie um pacote chamado utilidades curso em video que tenha dois modulos internos DADOS e MOEDAS 

transfira todas as funções utilizadas nos Desafio108, 109, 110 para o pacote moedas e mantenha tudo funcionando
'''
# from pacotes.moeda import Moeda

valor = 500

Moeda.resumo(valor, 20, 10)

print(f'{Moeda.dobro(valor)}')
print(f'{Moeda.metade(valor)}')
print(f'{Moeda.aumenta(valor,10)}')
print(f'{Moeda.diminui(valor, 20)}')

