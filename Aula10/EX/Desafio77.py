'''
Criado por: Gui Castro

25/01/2025
Crie  um programa que tenha uma tupla unica com os nomes de produtos e seus respectivos preços na sequencia. No final mostre uma listagem de preços, organizando os dados de forma tabular.
'''

listagem = ('Lápis', 3.45, 'Caderno', 100.00, 'Borracha', 3.0, 'Caneta', 8.0)

print('-' * 30)
print(f'{"Listagem De Preço"}'.center(30, '.'))
print('-' * 30)

for i in range(0, len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')  # Produto centralizado e com pontos
    else:
        print(f'R${listagem[i]:.2f}'.rjust(5))  # Valor formatado e alinhado à direita