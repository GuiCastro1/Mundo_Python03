'''
Criado por: Gui Castro

29/01/2025

Crie um programa que leia o nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos em uma lista no final mostre:

Quantas pessoas foram cadastradas

A média de idade do grupo

Uma lista com todas as mulheres

Uma lista com todas as pessoas com a idade acima da media = 45 
'''
dicionario = {}
lista = []
lista_di_muie=[]
lista_di_pessoas_acima_da_media = []
contador = 0
while True:

    dicionario['Nome'] = str(input('Nome:'))
    dicionario['Idade'] = int(input('Idade'))
    dicionario['Sexo'] = str(input('Sexo[M/F]')).strip().upper()[0]
    while dicionario['Sexo'] not in 'MF':
        dicionario['Sexo'] = str(input('Sexo[M/F]')).strip().upper()[0]
    contador += dicionario['Idade']
    lista.append(dicionario.copy())
    dicionario.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

media = contador/len(lista)

for i in lista:

    for k, v in i.items():

        if k == 'Sexo' and v == 'F':
            lista_di_muie.append(i['Nome'])

        if k == 'Idade' and v >= media:
            lista_di_pessoas_acima_da_media.append(i)
            
print('-='*30)
print(f'Foram cadastradas {len(lista)} Pessoas')
print(f'A média de idade do grupo{media:.2f}')
print(f'Todas as mulheres{lista_di_muie}')
print(f'As pessoas com a idade acima da media')
for i in lista_di_pessoas_acima_da_media:
    for k, v in i.items():
        print(f'{k} {v}', end=' ')
    print()
print('-='*30)
