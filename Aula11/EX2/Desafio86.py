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