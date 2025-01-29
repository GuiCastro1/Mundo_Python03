'''
Criado por: Gui Castro

26/01/2025

Crie um programa onde o usúario possa digitar vários valores numéricos a cadastre-os em uma lista. Caso o valor ja exista ele não deve ser cadastrados.No final mostre todos os valores digitados em ordem crescente.
'''
print('=====Números Unicos Na Lista =====')
lista = []
while True:

    valor = int(input('Digite um número:'))

    if valor in lista:
            print('Valor já cadastrado, cadastre outro')
    else:
            lista.append(valor)

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S / N]')).upper().strip()[0]
    
    if continua == 'N':
        break

lista.sort()
print(lista)