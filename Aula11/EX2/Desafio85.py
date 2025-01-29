'''
Criado por: Gui Castro 

27/01/2025

Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista.

Quantas pessoas foram cadastradas

Uma listagem com os mais pesados 

Uma listagem com os mais leves
'''
print('=====Lista de Pesos====')
lista = []
lista_aux = []
mai = men = 0

while True:

    nome = str(input('Digite seu nome:'))
    peso = float(input('Digite o peso:'))
    lista_aux.append(nome)
    lista_aux.append(peso)
    if len(lista) == 0:
        mai = lista_aux[1]
        men = lista_aux[1]
    else:
        if lista_aux[1] > mai:
            mai =lista_aux[1]

        if lista_aux[1] < men:
            men = lista_aux[1]

    lista.append(lista_aux[:])
    lista_aux.clear()

    continuar = str(input('Deseja continuar [S / N]:')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S / N]:')).strip().upper()[0]
    if continuar == 'N':
        break

# print(lista_aux)
print(lista)



print('-=' * 30)
print(f'Ao todo você cadastrou, {len(lista)} pessoas')
print(f'O maior peso foi de {mai} Kg',  end='')
for i in lista:

    if i[1] == mai:
        print(f'{i[0]}', end='')
print(f'O menor peso foi de {men} Kg' ,end='')

for i in lista:
    if i[1] == men:
        print(f'{i[0]}')