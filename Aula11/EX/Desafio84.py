'''
Criado por: Gui Castro

26/01/2025

Crie um programa que onde o usúario possa digitar um aexpressão qualque que use parentes. Seu aplicativo deverá analisar se a espressão pasada está com os parentes abertos e fechados na ordem correta.
'''
expressao = input('Digite um expressão').strip().upper()
abre = 0

for i in expressao:
    # if i == ')' and abre > 0:
    #     abre -=1

    # if i == '(':
    #     abre += 1
    if i == '(':
        abre += 1

    elif i == ')':
        if abre > 0:
            abre -= 1
        else: 
            abre -= 1
            break

if abre < 0 or abre % 2 == 1:

    print('expresão INCORRETA')

elif abre == 0:
    print('expresão CORRETA')


