from Biblioteca.Modulo import *
while True:

    resposta = menu(['Cadastrar Novas Pessoas', 'Ver a lista', 'Fechar Programa '])

    if resposta == 1:
        cabeçalho('Cadastrar Novas Pessoas')
    elif resposta == 2:
        cabeçalho('Ver a lista')
    elif resposta == 3:
        cabeçalho('Fechar Programa')
        cabeçalho('SAINDO, VOLTE SEMPRE ! ! !')
        break
    else:
        cabeçalho('ERRO! DIGITE UMA OPÇÃO VÁLIDA')