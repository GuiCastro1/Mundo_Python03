'''
Criado por: Gui Castro

30/01/2025

faça um programa que tenha um afunção chamada nota(). que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes inormações:

A quantidade de notas
A maior nota
A menor nota 
A média da turma 
A situação(opicional) de acordo com a media (RUIM, RAZOAVEL, OTIMA)
e fazer a DocString
'''

def nota(* num, Show =True):
    """
    A função nota rebece vários valores e retorna
    A quantidade de notas
    A maior nota
    A menor nota 
    A média da turma 
    A situação(opicional) de acordo com a media (RUIM, RAZOAVEL, OTIMA) se Show == True
    """
    notas = {}
    maior = menor = situacao = soma = 0
    lista = [num]

    for v in lista:

        for num,i in enumerate(v):

            soma += i

            if num == 0:
                maior = menor = i
            else:
                if i > maior:
                    maior = i
                if i < menor:
                    menor = i

    soma = soma / len(lista[0])

    if soma <= 5:
        situacao = 'RUIM'
    elif soma <= 7.9:  # Já sabemos que soma > 4 aqui
        situacao = 'RAZOAVEL'
    else:  # Se não for nenhuma das anteriores, só pode ser >= 8
        situacao = 'OTIMA'


    notas['Número_de_Notas'] = len(lista[0])
    notas['Maior'] = maior
    notas['Menor'] = menor
    notas['Média'] = soma
    if Show:
        notas['Situação'] = situacao

    return notas
t = nota(4, 4, 6, 4, 34)
print(t)
# print(nota(4, 4, 6, 4))
# print(nota(4, 4, 6, 4, 4, 65, 6, 1, 13, 54, 64 ))
# print(nota(4, 4, 6, 4, 34 ))
# print(nota(4, 4, 6, 4,  54, 23))
# print(nota(4, 4, 6, 4,  34))