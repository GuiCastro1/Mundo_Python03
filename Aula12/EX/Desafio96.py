'''
Criado por: Gui Castro

29/01/2025

Aprimore o desafio dos jogadores só que agora para vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento. de cada jogador.
'''
lista_de_jogadores= []
gols = []
dicio = {}
soma = 0 
while  True :
    dicio['Nome'] = str(input('Nome do jogador:'))
    num_partida = int(input('Nº de partidas:'))

    for i in range(1,num_partida + 1):
        i = int(input(f'Nº de gols da partida {i}ª:'))
        soma += i
        gols.append(i)

    dicio['Gols_partida'] = gols
    dicio['Soma_Gols'] = soma

    lista_de_jogadores.append(dicio.copy())
    i = 0
    soma = 0 
    gols = []
    dicio.clear()

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    if  cont == 'N':
        break
print('-='*30)
# Cabeçalho da tabela
print(f'{"Cod":<4} {"Nome":<10} {"Gols":<10} {"Total":<5}')

# Percorre a lista de jogadores
for i, v in enumerate(lista_de_jogadores):
    print(f'{i +1:<4}', end=' ')  # Exibe o índice do jogador

    # Exibe os valores do dicionário formatados
    for item in v.values():
        print(f'{str(item):<10}', end=' ')
    
    print()  # Quebra de linha após cada jogador

while True: 

    jogador = int(input('(1000 Para Sair)-Digite o codigo do jogador:'))
    jogador = jogador -1
    if jogador == 999:
        break
    if  jogador < 0 or jogador >= len(lista_de_jogadores):
        print('Codigo invalido tente novamente')
    else:
        print('-='*30)
        print(f'O Jogador {lista_de_jogadores[jogador]["Nome"]}')

        for i, v in enumerate(lista_de_jogadores[jogador]['Gols_partida']):
            print(f'Na {i + 1}º partida {lista_de_jogadores[jogador]["Nome"]} fez,{v}  Gols')
        print(f'Totalizando : {lista_de_jogadores[jogador]["Soma_Gols"]} Gols')
        print('-='*30)

print('O PROGRAMA ACABOU ! ! !')   