'''
Criado por: Gui Castro

29/01/2025

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior valor.

j 3
j 5
j 6
j 2

j 6
j 5
j 3
j 2
'''
from random import randint
from time import sleep
from operator import itemgetter
dicionario = {}
cont  = 1
for i in range(1,5):

    dicionario[f'Jodador{i}'] =  randint(1,6)

print('-=' * 30)
for k, v in dicionario.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ranking = []

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('-='* 15)
print(f'{"GANHADORES":^30}')
for i, v in enumerate(ranking):
    print(f'{i +1} lugar {v[0]} com {v[1]}')


ganhadores = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)

ganhadores = dict(ganhadores)
print('-='* 15)
print(f'{"GANHADORES":^30}')
for k, v in ganhadores.items():

    print(f'O {cont}º colocado foi o, {k} que tirou um {v}')
    cont += 1
    sleep(1.0)
print('-='* 15)
print(f'{"O PROGRAMA ACABOU ! ! !":^30}')

'''
Ambas as expressões fazem a mesma coisa: elas ordenam os itens de um dicionário com base nos valores, em ordem decrescente. No entanto, há uma diferença na forma como a chave de ordenação é definida:

1. Usando itemgetter(1)
python
Copiar
Editar
from operator import itemgetter

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
itemgetter(1) é uma função da biblioteca operator que retorna o segundo elemento de cada tupla (chave, valor).
Como dicionario.items() retorna uma lista de tuplas (chave, valor), o itemgetter(1) pega os valores e os usa para ordenar.
2. Usando lambda x: x[1]
python
Copiar
Editar
ganhadores = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)
lambda x: x[1] é uma função anônima que recebe um elemento (uma tupla (chave, valor)) e retorna x[1], ou seja, o valor do dicionário.
Isso também ordena com base nos valores, de forma idêntica ao itemgetter(1).
Então, qual a diferença?
itemgetter(1) é um pouco mais eficiente, pois evita a sobrecarga de criar funções anônimas dinamicamente.
lambda x: x[1] é mais flexível, permitindo modificações mais facilmente, como mudar a chave de ordenação para outra posição ou fazer cálculos adicionais.
Em resumo, para esse caso específico, ambos fazem a mesma coisa, mas itemgetter(1) pode ser ligeiramente mais rápido.



Uma função anônima é uma função que não tem nome. Em Python, usamos lambda para criar esse tipo de função.

Exemplo de uma função normal:
python
Copiar
Editar
def soma(a, b):
    return a + b

resultado = soma(2, 3)  # Retorna 5
Aqui, soma é o nome da função.

Exemplo de uma função anônima (lambda):
python
Copiar
Editar
soma = lambda a, b: a + b

resultado = soma(2, 3)  # Retorna 5
Nesse caso, a função não tem um nome explícito como def soma(), mas faz a mesma coisa.

Agora, voltando ao seu código:

python
Copiar
Editar
ganhadores = sorted(dicionario.items(), key=lambda x: x[1], reverse=True)
Aqui, lambda x: x[1] é uma função anônima que recebe um elemento x (que é uma tupla (chave, valor)) e retorna x[1] (o valor do dicionário).

Seria o mesmo que fazer:

python
Copiar
Editar
def pegar_valor(x):
    return x[1]

ganhadores = sorted(dicionario.items(), key=pegar_valor, reverse=True)
A vantagem do lambda é que você pode definir funções pequenas diretamente dentro de expressões sem precisar nomeá-las.



Usos de Funções Anônimas (lambda) na Vida Real
As funções anônimas (lambda) são úteis quando você precisa de uma função curta e temporária, sem precisar definir um nome para ela. Elas são muito usadas em:

Ordenação de listas e dicionários
Como já vimos, lambda é útil para definir a chave de ordenação:

python
Copiar
Editar
alunos = [
    {"nome": "Carlos", "nota": 8},
    {"nome": "Ana", "nota": 10},
    {"nome": "Bruno", "nota": 6}
]
# Ordenando por nota
ranking = sorted(alunos, key=lambda aluno: aluno["nota"], reverse=True)
print(ranking)
Filtros em listas (filter)
Para filtrar dados rapidamente sem precisar criar uma função nomeada:

python
Copiar
Editar
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]
Transformação de listas (map)
Para modificar cada elemento de uma lista de forma concisa:

python
Copiar
Editar
quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Redução de listas (reduce)
Para acumular valores sem criar uma função separada:

python
Copiar
Editar
from functools import reduce
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # 55 (soma de 1 a 10)
Diferença entre Função Anônima e Função Declarada
Característica	Função Anônima (lambda)	Função Declarada (def)
Nome	Não tem nome	Tem um nome específico
Uso	Para operações rápidas e temporárias	Para funções reutilizáveis e mais complexas
Número de expressões	Apenas uma expressão	Pode ter várias linhas de código
Legibilidade	Menos legível quando complexa	Mais fácil de entender
Reutilização	Não pode ser reutilizada fora do local onde foi definida	Pode ser chamada em vários lugares
Suporte a return	Retorna implicitamente o valor da expressão	Usa return explicitamente
Limitações das Funções Anônimas (lambda)
Só pode conter uma única expressão

python
Copiar
Editar
lambda x: x * 2  # OK
Mas não pode ter múltiplas instruções:

python
Copiar
Editar
lambda x: print(x); x * 2  # ❌ Isso dá erro!
Não pode conter estruturas de controle como if, for e while diretamente
Se precisar de lógica mais complexa, uma função def é melhor:

python
Copiar
Editar
def verificar_par(x):
    if x % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
Dificulta a depuração (debug)
Como lambda não tem nome, se ocorrer um erro, pode ser mais difícil de identificar no código.

Conclusão: Quando usar lambda ou def?
Use lambda para funções curtas e descartáveis, como ordenação e filtros rápidos.
Use def para funções reutilizáveis ou com lógica mais complexa.
Ou seja, se a função for pequena e só usada uma vez, lambda pode ser uma boa escolha. Se precisar de reutilização, manutenção ou mais de uma linha de código, use def.



No seu exemplo:

python
Copiar
Editar
soma = lambda a, b: a + b
print(soma(2, 3))  # 5

sub = 8 - 4
print(sub)  # 4
🔹 Usar lambda para operações simples como a + b não traz muita vantagem sobre fazer a conta diretamente.

Quando faz sentido usar lambda?
Se a operação precisar ser passada como argumento para outra função (ex: map, filter, sorted):

python
Copiar
Editar
numeros = [(1, 2), (3, 4), (5, 6)]
somas = list(map(lambda x: x[0] + x[1], numeros))
print(somas)  # [3, 7, 11]
Ou se quiser evitar criar uma função nomeada para algo pequeno:

python
Copiar
Editar
soma = lambda a, b: a + b
print(soma(10, 20))  # 30
Quando NÃO faz sentido usar lambda?
Se a expressão for simples e direta, usar uma variável comum é mais legível:

python
Copiar
Editar
sub = 8 - 4
print(sub)  # 4
Ou se precisar reutilizar a função mais tarde:

python
Copiar
Editar
def soma(a, b):
    return a + b

print(soma(10, 20))  # 30
✅ Conclusão: Para expressões simples, usar lambda ou variáveis diretas não faz muita diferença, mas lambda é útil quando a função precisa ser passada como argumento ou escrita inline.
'''