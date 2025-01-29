'''
Criado por: Gui Castro

26/01/2025

Crie um programa que leia vários números e coloque na lista.Depois disso crie duas listas extras que vão conter apenas os valores ímpares eos valores pares digitados, respectivamente.
'''
lista = []
pares = []
impar = []

while True:

    lista.append(int(input('Digite um número:')))

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S / N]')).upper().strip()[0]
    
    if continua == 'N':
        break

for i in lista:

    if i % 2 == 0:
        pares.append(i)
    else:
        impar.append(i)
print(lista)
pares.sort()
impar.sort()

print(f'PARES = {pares}')
print(F'ÍMPARES = {impar}')
