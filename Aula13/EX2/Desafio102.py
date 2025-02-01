'''
Criado por: Gui Castro

30/01/2025

Crie um programa que tenha uma função chamada voto(). Que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um avlor literal indicando se uma tem voto NEGADO, OPICIONAL e OBRIGATORIO nas eleições.
'''
# from datetime import date
# def voto(idade):

#     if idade >= 65:
#         return 'OPICIONAL'
#     elif idade >= 18 and idade <=64:
#         return 'OBRIGATÓRIO'
#     elif idade < 18:
#         return 'NÃO VOTA'

# user = int(input('Digite sua data de nascimento:'))

# ano = date.today().year - user

# resposta = voto(ano)

# print(f'Você tem {ano}, e seu voto é {resposta}')

def voto(ano):
    # A  BIBLIOTECA E IMPOTADA MAS SO FUNCIONA NA FUNÇÃO DESSA MANEIRA ECONOMIZA MAIS MEMORIA JA QUE ELE SO SERVE NESSE ESCOPO
    from datetime import date
    
    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18  or idade > 65:
        return f'Com {idade} anos: OPICIONAL'
    else:
        return f'Com {idade} anos: OBRIGATÓRIO'