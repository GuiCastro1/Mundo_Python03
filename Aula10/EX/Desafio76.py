'''
Criado por: Gui Castro

25/01/2025

Desenvolva um programa que leia um programa que leia quatro valores pelo teclado e guade-os em uma tupla. No final mostre:

Quantas vezes apareceu o 9
Em que posição foi digitado o 1º valor 3 se não tiver o 3 mostrar mensagem 404
Quais fora os pares
'''
print('=====Tupla Com Verificação De Número=====')

tupla = ()

for i in range(1, 5):

    num = int(input('Digite um numero'))

    tupla = tupla + (num,)

print(f'O número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O número 3 apareceu {tupla.index(3) +1 } ª posição')

else:
    print(f'O número 3 não aparece nenhuma vez')

print('Valores pares digitados:', end=' ')

for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
