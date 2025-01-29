'''
Criado por: Gui Castro

25/01/2025

Crie um programa que tenha uma tupla com varias palavras(Não use acentos). depois mostre a voal de cada palavra
'''
print('=====PEGANDO VOGAIS DE PALAVRA=====')

lista = ('Bom', 'Dia', 'Teste')
vogal = ()

for i in lista:

    print(f'\nNa palavra {i.upper()} temos :', end='')

    for g in i:
            
        if g.lower() in 'aeiou':

            print(g,end='')
                