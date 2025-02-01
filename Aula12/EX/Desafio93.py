'''
Criado por: Gui Castro

29/01/2025

Crie um programa que leia nome ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for != de zero, o dicionario receberá também o (ano de contratação e o salário). Calcule e acrescente , alem da idade com quantos a pessoa vai se aposentar.
'''
from datetime import date

dicionario = {}
dicionario['Nome'] = str(input('Nome:'))
Ano =  int(input('Ano de Nascimento:'))
dicionario['Data'] = date.today().year - Ano
dicionario['Carteira'] = int(input('(Caso não tenha 0)Digitos da CTPS:'))

if dicionario['Carteira'] == 0:
    print('-=' * 30)
    for k,v in dicionario.items():
        print(f'O valor {k} tem {v}')

else:

    dicionario['Ano_Contatação'] = int(input('Ano de contratação'))
    dicionario['Salário'] = float(input('Salário:R$ '))
    dicionario['Apos'] = dicionario['Data'] + ((dicionario['Ano_Contatação'] + 35) - date.today().year)
    for k,v in dicionario.items():
        print(f'O valor {k} tem {v}')
    