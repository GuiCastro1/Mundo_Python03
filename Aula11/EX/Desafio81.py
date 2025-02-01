'''
Criado por: Gui Castro

26/01/2025

Crie um programa que onde o usúario possa digitar 5 números e coloque-os em uma lista.Já na posição correta de inserção sem usar o sort.No final mostre a lista ordenada
'''
lista = []

for i in range(0, 5):

    n = int(input('Digite um valor:'))
    if i == 0 or n > lista[-1]:
        print('Adicionando ao final da lista ...')
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista ...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram:{lista}')
