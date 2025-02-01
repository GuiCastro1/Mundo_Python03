'''
Criado por: Gui Castro

30/01/2025

Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valo res inteiros. Seu programa tem que analisar todos os valores e dizer qual é o maior
'''
from random import randint
def traso():
    print('-' * 60)


def maior(*numero):
    m = 0
    for i , v in enumerate(numero):
        if i == 0 or v > m:
            m = v
    traso()
    print(f'Você me passou os valores', end='')
    for valor in numero:
        print(valor, end=' ')
    print()
    print(f'E o maior e {m}')
    traso()

valor = [randint(1,50) for i in range(10)]

maior(* valor)
