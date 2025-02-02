'''
Criado por: Gui Castro

31/01/2025

Crie um módulo chamado moeda.py que tenha funções incorporadas. Aumentar() Diminuir() Dobro() e Metade()

Faça tambem um proragrama que importe e use esse módulo 
'''
from pacotes.moeda import Moeda

valor = 100

print(f'O dobro de {valor} é: {Moeda.dobro(valor)}')
print(f'A metade de {valor} é: {Moeda.metade(valor)}')
print(f'O {valor} mais 20% é: {Moeda.aumenta(valor,10)}')
print(f'O {valor} menos 20% é: {Moeda.diminui(valor,20)}')