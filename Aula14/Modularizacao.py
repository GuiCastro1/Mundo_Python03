'''
Surgiu no início de 60

Sistemas ficando maior

Foco:Dividir um programa grande

Foco: Aumentar a legibilidade

Foco: faciliatar a manutenção

Vantagens
Organização do código
Facilita manutenção
O cultação do código detalhado
Reutilização em outros projetos

pacote

Rever a aula e teste pacotes
'''
from uteis import fat
#Nesse caso pode ocorrer conflitos se tiver outra lib com o mesmo nome então opte por importar a linb toda import uteis
num = int(input('Digite um valor'))
fatorial = fat(num)
print(f'O fatorial de {num} é {fatorial}')