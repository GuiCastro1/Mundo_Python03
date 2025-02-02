def dinheiro(msg):

    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO {entrada} inválida')
        else:
            valido = True
            return float(entrada)