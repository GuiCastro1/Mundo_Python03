'''
Criado por: Gui Castro

31/01/2025

Modifique as funções do Desafio108 para que elas aceitem um parâmetro mais um valo, informando se o valor retornado por elas vai ser ou não formatado pela função moeda, desenvolvida no Desafio109
'''
from pacotes.moeda import Moeda

valor = 300

print(f'O dobro de {Moeda.moeda(valor)} é:{Moeda.dobro(valor, form=True)}')
print(f'A metade de {Moeda.moeda(valor)} é:{Moeda.metade(valor, form=True)}')
print(f'O valor {Moeda.moeda(valor)} mais 20% é:{Moeda.aumenta(valor,10, form=True)}')
print(f'O valor {Moeda.moeda(valor)} menos 20% é:{Moeda.diminui(valor, 20,form=True)}')