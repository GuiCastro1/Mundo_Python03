'''
Criado por: Gui Castro

25/01/2025

Crie uma tupla com os 20 primeiros colocados do Campeonato de futebol na ordem de colocação. Depois mostre:

Apenas os 5 primeiros colocados

Os 4 últimos 

Uma lista com os times em ordem alfabetica

Em que posição está o tima da chapecoense
'''
times_brasileirao_2018 = (
    "Atlético-MG", "Atlético-PR", "Bahia", "Botafogo", "Ceará",
    "Chapecoense", "Corinthians", "Cruzeiro", "Flamengo", "Fluminense",
    "Grêmio", "Internacional", "Palmeiras", "Paraná", "Santos",
    "São Paulo", "Sport", "Vasco", "Vitória", "América-MG"
)

print(sorted(times_brasileirao_2018))

print(f'Os 5 primeiros colocados foram: {times_brasileirao_2018[:5]}')

print(f'Os 4 ultimos foram: {times_brasileirao_2018[-4:]}')

for n, i in enumerate(times_brasileirao_2018):

    print(n)
    if i == 'Chapecoense':

        print(f'A Chapecoense esta em {n +1}ª na lista')

print(f'A Chapecoense esta em {times_brasileirao_2018.index('Chapecoense') + 1}ª na lista')
