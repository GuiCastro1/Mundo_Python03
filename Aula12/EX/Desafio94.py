'''
Criado por: Gui Castro

29/01/2025

Crie um programa que gerencie de um jogador de futebol. O programa vai ler o nome quantas partidas e gols por partida. No final tudo será guardado em um dicionário, incluindo o total de gols feitos no campeonato
'''
dicinario = {}
gol = []
# lista = []
soma = 0

dicinario['Nome'] = str(input('Nome do jogador:'))
dicinario['Número_Partida'] = int(input('Nº de partda'))
for i in range(1,dicinario['Número_Partida'] +1):

    i = int(input(f'N° de gols {i}ªpartida:'))
    gol.append(i)
    soma += i

dicinario['Gols_Por_Partida'] = gol 
dicinario['Número_de_Gols'] = soma

print('-='*30)
print(dicinario)
print('-='*30)
for k, v in dicinario.items():
    print(f'Ocampo {k}, tem o valor: {v}')
print('-='*30)
for i, v in enumerate(dicinario['Gols_Por_Partida']):
   print(f'Na partida {i+1} o {dicinario["Nome"]}, fez {v}')
print(f'Total de gols {dicinario["Número_de_Gols"]}')