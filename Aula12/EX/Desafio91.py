'''
Criado por: Gui Castro

29/01/2025

Crie um programa que leia nome e media de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
'''
dicionario = {}

dicionario['Nome']= str(input('Nome do aluno:'))
dicionario['Media']= float(input(f'Qual e a média de {dicionario["Nome"]}'))

if dicionario['Media'] < 5:

    dicionario['Situação'] = 'REPROVADO'

elif dicionario['Media'] >= 5:

    dicionario['Situação'] = 'APROVADO'

print('-='*30)

for k , v in dicionario.items():

    print(F'{k} = {v}')
