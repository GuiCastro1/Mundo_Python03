'''
Criado por: Gui Castro

25/01/2025

Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.

Depois mostre a listagem dos números gerados e indique qual é o maior e o menor
'''
print('=====Maior e Menor Tupla=====')
from random import randint
lista = ()
maior = menor = 0

for i in range(1, 6):

    num = randint(1, 100)
    
    lista = lista + (num,)

for g in lista:

        if  maior == 0 and menor == 0:
            maior =  g
            menor = g
        else:
            if g > maior:
                maior = g
            if g < menor:
                menor = g

print(lista)
print(maior)
print(menor)


n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
print(n)
print(max(n))
print(min(n))