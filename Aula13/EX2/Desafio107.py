'''
Criado por: Gui Castro

30/01/2025

Faça um mini sistema que utilize o InterativeHelp do Python. O usúario vai digitar o comando e o manual vai aparecer. Quando o user digitar 'FIM', o programa se encerrará.
'''
from time import sleep

def ajuda(comando):
    help(comando)
    sleep(1.5)

def titulo(msg):

     tam = len(msg) + 4

     print('~' * tam)
     print(f'  {msg}')
     print('~' * tam)

     sleep(1.5)


#principal

comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP ! ! !')
    comando = str(input('Função ou Biblioteca'))
    if comando == 'FIM':
        break
    else:
        ajuda(comando)

titulo('O PROGRAMA ACABOU ! ! !')