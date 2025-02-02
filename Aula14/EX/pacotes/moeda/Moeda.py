# def dobro(n):
#     return n * 2

# def metade(n):
#     return n / 2

# def aumenta(n):
#     return n + ((n * p) / 100)

# def diminui(n):
#     return n - ((n * p) / 100)


###############################################
# def dobro(n, form=False):
#     if form:
#         return moeda(n)
#     return n * 2

# def metade(n, form=False):
#     if form:
#         return moeda(n)
#     return n / 2

# def aumenta(n, p, form=False):
#     if form:
#         return moeda(n)
#     return n + ((n * p) / 100)

# def diminui(n, p, form=False):
#     if form:
#         return moeda(n)
#     return n - ((n * p) / 100)

# def moeda(n):
#     return f'R${n:.2f}'

# def resumo(n, a, d):

#     print(f'-'*20)
#     print(f'{"RESUMO":^20}')
#     print(f'-'*20)
   
#     print(f'Dobro de {moeda(n)} é: {dobro(n)}')
#     print(f'Metade de {moeda(n)} é: {metade(n)}')
#     print(f'Aumento de {a}% em {moeda(n)} é: {aumenta(n, a)}')
#     print(f'Desconto de {d}% em {moeda(n)} é: {diminui(n, d)}')
def dobro(n, form=True):
    resultado = n * 2
    return moeda(resultado) if form else resultado

def metade(n, form=True):
    resultado = n / 2
    return moeda(resultado) if form else resultado

def aumenta(n, p, form=True):
    resultado = n + ((n * p) / 100)
    return moeda(resultado) if form else resultado

def diminui(n, p, form=True):
    resultado = n - ((n * p) / 100)
    return moeda(resultado) if form else resultado

def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

def resumo(n, a, d):

    print(f'-'*20)
    print(f'{"RESUMO":^20}')
    print(f'-'*20)
    print(f'Valor analisado:{n}')
    print(f'Dobro é:\t{dobro(n)}')
    print(f'Metade é:\t{metade(n)}')
    print(f'Aumento {a}% é:\t{aumenta(n, a)}')
    print(f'Desconto {d}% é:\t{diminui(n, d)}')
