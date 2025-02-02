'''
Criado por: Gui Castro

31/01/2025

No pacote do curso em video adicione uma função oa modulo dado. Chamada leiadinheiro() que seja capaz de funcionar como a função input() mas com validação de dados para aceitar apenas valores monetarios aceitar ,,,,,,
'''
from pacotes.dados import format_din_din
from pacotes.moeda import Moeda

p = format_din_din.dinheiro('Digite o preço R$:')

Moeda.resumo(p, 10, 40)

