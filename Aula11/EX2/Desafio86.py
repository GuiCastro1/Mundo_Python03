'''
Criado por: Gui Castro 

27/01/2025

Crie um programa que receba 7 números do usúario e coloque-os em uma lista única  que mantenha os valores pares separodas dos ímpares. No final mostre pares e ímpares em ordem crescente.
'''
lista = []
aux = []
aux_da_aux = []
for i in range(1,8):

    num = int(input('Digite um número'))

    if num % 2 == 0:
        aux_da_aux.append(num)

    if num % 2 == 1:
         aux.append(num)

lista.append(aux_da_aux[:])
lista.append(aux[:])
print(lista)
'''
correção guanabara
lista = [[], []]

for i in range(1, 8):

    num = int(input(f'Digite o {i}º valor:'))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()
print(lista)

print(f'Os números de pares foram, {lista[0]}')
print(f'Os números de ímpares foram, {lista[1]}')
'''

'''

    aux = []

for i in range(1,8):

    num = int(input('Digite um número'))

    if num % 2 == 0:
        lista.append(num)

    if num % 2 == 1:
         aux.append(num)

lista.append(aux[:])
print(lista)


'''