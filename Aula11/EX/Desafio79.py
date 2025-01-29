'''
Criado por: Gui Castro

26/01/2025

Faça um programa que leia 5 números e os guarde em uma lista. No final mostre o maior e o menor valor e suas posições. Se tiver mais de um mostrar as duas posições
'''
'''
print('=====Maior & Menor Na Lista=====')
lista = []
maior = menor = 0
for i in range(1, 6):
    lista.append(int(input('Digite um número:')))

for i in lista:

    if maior == 0 and menor == 0:
        maior = i
        menor = i
    else:
        if i > maior:
            maior = i
            
        if i < menor:
            menor = i
            
lista.sort()
print(lista)
print(max(lista))
print(min(lista))
print(f'O maior número da lista{maior} esta na posição {lista.index(maior)}')
print(f'O menor número da lista{menor} esta na posição {lista.index(menor)}')
'''

listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um número na posição {c}:  ')))

    if c == 0 :
        maior = listanum[c]
        menor = listanum[c]

    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]

print(f'Você digitou os valores {listanum}')

print(f'O maior valor foi  {maior} na posição ', end='')


for i, v in enumerate(listanum):

    if v == maior:
        print(f'{i}...',end='')

print(f'O menor valor foi {menor} na posição ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...')
