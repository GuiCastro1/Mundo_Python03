'''
Criado por: Gui Castro 

27/01/2025

Crie um programa que crie uma matriz 3 x 3 e preencha com os valores lidos pelo teclado. No final mostre com formatação correta.
'''
#meu
lista = []
lista_aux = []
for i in range (1,10):

    v = int(input('Digite um valor:'))
    lista_aux.append(v)

    if len(lista_aux) % 3 == 0:
        lista.append(lista_aux[:])
        lista_aux.clear() 

for i in lista:
    print(i)

#gaunabara
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0,3):

        matriz [l] [c] = int(input(f'Digite um número[ {l}:{c}]'))

print('-=' * 30)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()