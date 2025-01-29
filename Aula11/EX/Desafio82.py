'''
Criado por: Gui Castro

26/01/2025

Crie um programa que vai ler vários números e colocar em uma lista.

Quantos números foram digitados 

A lista de valores ordenada em ordem decresente

e se o valor 5 foi digitado e esta ou não na lista
'''
print('=====Extraindo Dados De Uma Lista=====')
lista = []
contador = 0
while True:

    lista.append(int(input('Digite um número:')))

    contador += 1

    continuar = str(input('Deseja continuar:[ S / N]')).strip().upper()[0]

    if continuar == 'N':
        break

#mas há um pequeno detalhe no uso do método sort(). O método sort() não retorna uma nova lista, ele modifica a lista original in-place e retorna None. Por isso, ao usar lista.sort(reverse=True) diretamente na f-string, você verá None na saída.
lista.sort(reverse=True)
print(f'Você digitou {contador} números')
print(f'Você digitou {len(lista)} números')
print(f'lista em ordem decresente:{lista}')

if 5 not in lista:
    print(f'O valor 5 não faz parte da lista')
elif 5 in lista:
    print(f'O valor 5 aparece na lista na posição{lista.index(5)}')
