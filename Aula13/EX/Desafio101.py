'''
Criado por: Gui Castro

30/01/2025

Faça uma lista chamada números e duas funções chamadas sorteia o somaPar. A primeira função vai sortear 5 numeros e colocalos na lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

def sorteia():
    lista = [randint(1,50) for i in range(10)]
    #Correção do uso do map → map(lambda i: i % 2 == 0, lista) retorna uma lista de True ou False, então substituí por filter, que mantém apenas os valores que satisfazem a condição.
    par = list(filter(lambda i: i % 2 == 0, lista))
    print(lista)
    print(par)
sorteia()
'''
from random import randint
def l():
    print('-' * 60)


def sorteia():
    lista = [randint(1,50) for i in range(10)]
    l()
    print(f'A lista gerada:',end=' ')
    for p_l in lista:
        print(p_l, end=' ')
    print()
    l()
    return lista

def soma(lista):

    par = list(filter(lambda x : x % 2 == 0, lista))
    l()
    print(f'A nova lista só com paresa:', end=' ')
    for pgv in par:
        print(pgv, end=' ')
    print()
    l()
    soma = 0
    for i in par:
        soma += i
    print(f'A soma de pares é {soma}')
    print(f'A soma de pares é {sum(par)}')
    l()

lista_sorteada = sorteia()
soma(lista_sorteada)

# from random import randint

# # Função para exibir a linha divisória
# def l():
#     print('-' * 60)

# # Função que sorteia os números e retorna a lista
# def sorteia():
#     lista = [randint(1, 50) for _ in range(10)]
#     l()
#     print(f'A lista gerada:', ' '.join(map(str, lista)))  # Exibe os números lado a lado
#     l()
#     return lista

# # Função que soma os pares e exibe o resultado
# def soma(lista):
#     pares = list(filter(lambda x: x % 2 == 0, lista))  # Filtra os números pares
#     l()
#     print(f'A nova lista só com pares:', ' '.join(map(str, pares)))  
#     print(f'A soma dos pares é {sum(pares)}')  # Exibe a soma diretamente
#     l()

# # Executando as funções
# lista_sorteada = sorteia()
# soma(lista_sorteada)


'''
O seu código tem um erro porque a função sorteia(lista) não retorna a lista gerada, ela apenas a imprime. Além disso, ao chamar soma(sorteia(lista)), a segunda chamada de sorteia(lista) não retorna um valor válido, resultando em um erro ao tentar filtrar os números pares.

🛠 Correção
Para corrigir isso, você deve fazer a função sorteia(lista) retornar a lista sorteada e passar esse retorno para a função soma(lista), assim:

python
Copiar
Editar
from random import randint

def sorteia():
    lista = [randint(1, 50) for _ in range(10)]  # Gera a lista aleatória
    print("Lista sorteada:", lista)
    return lista  # Retorna a lista

def soma(lista):
    pares = list(filter(lambda x: x % 2 == 0, lista))  # Filtra apenas os pares
    print("Números pares:", pares)
    print("Soma dos pares:", sum(pares))  # Soma os pares

# Agora chamamos a função corretamente
lista_sorteada = sorteia()  # Guarda a lista retornada
soma(lista_sorteada)  # Passa a lista para a função soma
✅ Principais correções:
Agora sorteia() retorna a lista gerada, permitindo que a função soma() a utilize corretamente.
Usei sum(pares) para calcular a soma dos números pares, que provavelmente era o objetivo.
Corrigi a chamada de sorteia(lista) → Agora usamos sorteia() corretamente, sem passar um argumento desnecessário.
Removi a variável lista = [] desnecessária, pois a função sorteia() já gera uma nova lista.
🔹 Saída esperada (exemplo)
yaml
Copiar
Editar
Lista sorteada: [23, 14, 7, 42, 9, 18, 33, 12, 27, 6]
Números pares: [14, 42, 18, 12, 6]
Soma dos pares: 92
Agora seu código funciona corretamente!
from random import randint
def sorteia(lista):
    lista = [randint(1,50) for i in range(10)]
    print(lista)

def soma(lista):
    par = list(filter(lambda x : x % 2 == 0, lista))
    print(par)

lista = []
sorteia(lista)
soma(sorteia(lista))
'''

