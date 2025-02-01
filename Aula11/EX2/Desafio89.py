'''
Criado por: Gui Castro 

27/01/2025

faça um programa que ajudeum jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números de 1 a 60para cada jogo. cadas trando tudo em uma lista composta.
'''
from random import randint
from time import sleep
lista = []
aux = []
print('-=' * 15)
print(f'{'MEGA SENA':^30}')
print('-=' * 15)

# jogos = int(input('Quntos jogos deseja fazer:'))

# for i in range(0, jogos):
#     aux = [randint(1,60),randint(1,60),randint(1,60),
#                     randint(1,60),randint(1,60),randint(1,60),]

   
#     lista.append(aux[:])
#     aux.clear()

# for i in lista:
#     print(i)
#     sleep(0.5)

# print('BOA SORTE ! ! !')

jogo = int(input('Digite o número de jogos que deseja realizar:'))

while True:

    numero = randint(1,60)

    if numero not in aux:
        aux.append(numero)

    if len(aux) == 6:
            aux.sort()
            lista.append(aux[:])
            aux.clear()

    if len(lista) == jogo:
        break

for i, v in enumerate(lista):

    print(f'Jogo{i + 1}: {v}')
    sleep(0.5)
    
print('-=' * 15)
print(f'{'BOA SORTE ! ! !':^30}')
print('-=' * 15)
    # if len(aux) == jogo * 6:
    #     break
'''
Para evitar números repetidos na lista aux, você pode usar um laço while ou um conjunto (set) para garantir que os números gerados sejam únicos antes de adicioná-los à lista.

O processo seria:

Criar uma estrutura para armazenar os números temporariamente.
Gerar números aleatórios até que o total desejado seja atingido.
Verificar se o número já está na estrutura antes de adicioná-lo.
Depois que a estrutura conter a quantidade correta de números, adicioná-la à lista.






Você disse:
como estou indo?jogo = int(input('digite um número:'))

while True:

    numero = randint(1,60)

    if numero not in aux:
        aux.append(numero)

    if len(aux) == jogo * 6:
        break

for i in aux:
    
    if i % 6 == 0:

        lista.append(aux[:])

for i in lista:
    print(i)
O ChatGPT disse:
ChatGPT
Seu código tem alguns problemas de lógica e estrutura. Aqui estão os pontos que precisam ser corrigidos:

Erros e melhorias
randint(1,60) não está importado

Você precisa importar randint do módulo random.
aux não foi inicializada antes do while

A variável aux precisa ser uma lista vazia antes do loop.
Condição de parada no while está errada

Você está multiplicando jogo * 6, mas isso geraria todos os números em uma única lista, em vez de criar várias apostas separadas.
Erro na lógica de adição à lista

O segundo for não faz sentido. Você está verificando i % 6 == 0, mas isso não é necessário.
O correto seria dividir aux em apostas de 6 números antes de adicionar à lista.
Se sua intenção era criar apostas com 6 números únicos para cada jogo, a lógica correta seria:

Para cada jogo, gerar 6 números únicos.
Adicionar cada conjunto de 6 números à lista.
Exibir os jogos gerados no final.
Se precisar de mais dicas ou quiser rever seu código corrigido, me avise! 🚀







Você disse:
from random import randint
from time import sleep
lista = []
aux = []

jogo = int(input('digite um número:'))

while True:

    numero = randint(1,60)

    if numero not in aux:
        aux.append(numero)

    if len(aux) % 6 == 0:
            lista.append(aux[:])
            aux.clear()

    if len(lista) == jogo:
        break


for i in lista:

    print(i)
    sleep(0.5)
O ChatGPT disse:
ChatGPT
Seu código está quase correto, mas há um pequeno erro na forma como os números são adicionados à lista.

Erros e melhorias
Problema na divisão dos números em jogos separados:

Você está verificando if len(aux) % 6 == 0, mas isso pode causar um erro se aux já estiver vazia.
O ideal é verificar if len(aux) == 6 antes de adicioná-la à lista.
Uso correto do clear():

aux.clear() está correto, mas é importante garantir que ele só seja chamado depois que aux já tiver 6 números.
Correção da lógica
Criar jogo apostas, cada uma contendo 6 números únicos.
Quando aux atingir 6 números, adicioná-la à lista e esvaziá-la.
Repetir até gerar a quantidade desejada de jogos.
Exibir os jogos ao final.
Se quiser testar a versão corrigida, me avise! 🚀







Você disse:
jogo = int(input('digite um número:'))

while True:

    numero = randint(1,60)

    if numero not in aux:
        aux.append(numero)

    # if len(aux) % 6 == 0:
    if len(aux) == 6:
            lista.append(aux[:])
            aux.clear()

    if len(lista) == jogo:
        break


for i in lista:

    print(i)
    sleep(0.5)
O ChatGPT disse:
ChatGPT
Agora seu código está quase perfeito, mas há um detalhe importante:

Problema
O código está gerando corretamente jogo apostas, mas os números em cada aposta não estão ordenados.

Na maioria das loterias (como a Mega-Sena), os números costumam ser exibidos em ordem crescente.
Isso não afeta a lógica do sorteio, mas melhora a apresentação e organização.
Melhoria sugerida
Antes de adicionar aux à lista, ordene os números com sorted(aux).

Isso garante que os números de cada aposta sejam sempre apresentados organizados.

Se quiser, posso te mostrar como fica com essa melhoria. 🚀

'''