'''
Criado por: Gui Castro 

27/01/2025

Aprimore o desafio anterior mostrando no final:

A soma de todos os números pares

A soma dos valores da 3º coluna

O maior valor da 2º linha
'''
lista = []
lista_aux = []
for i in range(1, 10):
    num = int(input('Digite um número:'))
    lista_aux.append(num)

    if len(lista_aux) % 3 == 0:
        lista.append(lista_aux[:])
        lista_aux.clear()

soma = 0
for i in lista:
    print(i)
print('#' * 30)
for par in lista:
    
    for num in par:

        if num % 2 == 0:

            soma += num

print(f'A soma de todos os números pares é {soma}')
print('#' * 30)
soma_terceira_coluna = 0
for i in lista:

    soma_terceira_coluna += i[2]

print(f'A soma de todos os números da terceira coluna é {soma_terceira_coluna}')
print('#' * 30)
maior = 0
for i in lista[1]:

    maior = i

    if i > maior:
        maior = i

print(f'O maior número da segunda coluna é {maior}')
