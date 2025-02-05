def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Erro ! ! !. Digite um número inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('\n O usúario não digitou nenhum valor')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('Sistema de Anotações')
    cont = 1
    for i in lista:
        print(f'{cont} - {i}')
        cont += 1
    print(linha())
    opcao = leiaint('Sua opção:')

    