'''
Criado por: Gui Castro

31/01/2025

Adapte o código do Desafio108 criando uma função adicional chamada moeda que consiga receber os valores com um valor monetário e formatado
'''
from pacotes.moeda import Moeda

valor = 200

print(f'O dobro de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.dobro(valor))}')
print(f'A metada de {Moeda.moeda(valor)} é {Moeda.moeda(Moeda.metade(valor))}')
print(f'O valor {Moeda.moeda(valor)} mais 15% é {Moeda.moeda(Moeda.aumenta(valor,15))}')
print(f'O valor {Moeda.moeda(valor)} menos 20% é {Moeda.moeda(Moeda.diminui(valor,20))}')
