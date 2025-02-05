'''
Criado por: Gui Castro

01/01/2025

Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade e em um arquivo de texto simples. 

o programa vai ter duas funções cadstar e listar todas as pessoas
''' 
from Modulo import titulo,regex,arquivo,adiciona,le_arquivo
from time import sleep

titulo('MINI-SISTEMA')
titulo('Criando Lista . . . . .')

while True:
    nome = str(input('Nome da lista:'))
    resultado = (regex(nome))
    if resultado:
        break

nome_do_arquivo = arquivo(resultado)

while True:

    print('''
    1 - Cadastrar Novas Pessoas
    2 - Ver a lista
    3 - Fechar Programa 
    ''')

    escolha = str(input('Opção:'))

    while escolha not in '123':
        print('''
        1 - Cadastrar Novas Pessoas
        2 - Ver a lista
        3 - Fechar Programa 
        ''')
        sleep(1)
        escolha = str(input('Opção inválida:'))

    if escolha == '1':
        titulo('Cadastro')
        adiciona(nome_do_arquivo)
        sleep(1)
        
    elif escolha == '2':
        titulo('Lista')
        le_arquivo(nome_do_arquivo)
        sleep(1)
        
    else:
        titulo('Saindo . . .')
        sleep(1)
        break

titulo('O Programa Acabou ! ! ! ! !')
    