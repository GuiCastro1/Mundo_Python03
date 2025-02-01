'''
Criado por: Gui Castro

30/01/2025

Crie um programa que tenha uma função chamada fatorial(). Que receba dois parâmetros o 1º para o número e o outro chamado show, que será um valor lógico opicional(), indicando se o será mostrado ou não na tela o processo de calculo do fatorial
Fazer DocString
'''
from math import factorial
def linha():
    print('-=' * 30)


def fatorial(num , show=False):
    """
    OI
    """
    fac = factorial(num)

    if show:
        cont = num
        linha()
        while cont > 1:
            print(f'{cont} x', end= ' ')
            cont -= 1
        print(f' 1 = {fac}')
    linha()
    return fac

num = int(input('Digite um número para mostrar seu fatorial'))

conta = str(input('Deseja a exibição da conta [S / N]')).strip().upper()[0]

if conta == 'S':
    resultado = fatorial(num, show=True)
    print("Resultado:", resultado)
else:
    resultado = fatorial(num, show=False)
    print("Resultado:", resultado)
help(fatorial)