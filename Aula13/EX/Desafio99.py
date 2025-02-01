'''
Criado por: Gui Castro

30/01/2025

Faça um programa que tenha uma função chamada contador que receba três parâmetros:(INICIO, FIM E PASSO) e realize a contagem. Seu programa tem que realizar três contagens através da função criada:

A) de 1 a 10, de 1 em 1
B) de 10 a 0, de 2 em 2
C) uma contagen personalizada

comportamentos:

se passo == 0:
passo = 1

aceite negativos no passo e para o fim e começo
'''
from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p =1
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
                print(f'{cont} ', end='', flush=True)
                sleep(0.5)
                cont -= p
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem ! ! !')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(ini, fim, pas)