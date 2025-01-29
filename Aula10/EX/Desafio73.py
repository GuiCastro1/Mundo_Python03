'''
Criado por: Gui Castro

25/01/2025

Crie um programa que tenha uma tupla com uma contagem de 0 a 20 escrita por extenso. Seu programa deverá ler um número de 0 a 20 pelo teclado e exibir ele por extenso
'''
print('=====Lendo Número na Tupla=====')

lista_por_extenso = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dizesseie', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número de 0 a 20'))
    if 0 <= num <= 20:
        print(f'O número {num} se escreve {lista_por_extenso[num]} por extenso')
        break