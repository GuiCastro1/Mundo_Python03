def leiaint(num):
    while True:
        try:
            n = int(input(num)) 
        except (ValueError, TypeError):
            print('ERRO ! ! !, Digite um valor inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('\n O Usúario não digitou nenhum valor')
        else:
             return n

def leiafloat(num):

    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('ERRO ! ! !, Digite um valor real válido.')
            continue
        except(KeyboardInterrupt):
            print('\n O Usúario não digitou nenhum valor')
        else:
             return n
