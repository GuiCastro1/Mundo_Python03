'''
Interactive Help

# help(print)
# print(input.__doc__)

DocStrings
def oi(t)
    """
    A função oi retortna o texto que ela recebe com parâmetro
    """
    print(t)

oi('Hello, World ! ! ! ! !')

Argumentos Opicionais

def som(a = 0, b = 0, c = 0,)

    s = a + b + c
    print(s)

som(2,3,3)
som(15,23,15)
som(15,5,6)
som(15,5)
som(15,5)
som(15,5)
som(15)
som(15)
som(15)

Escopo de variáveis
def t():
    global n 
    n = 10
    x =9
    print(x)
    print(n)

# global n faz que o n de fora tenha o valor que foi declarado dentro da função
# local só vale na def e só pode ser usado la
# variaveis locais podem ter o mesmo nome e ter valoraes !=
# n e global vale na def
n = 5

print(x)

Retorno de resultados









'''

def som(a = 0, b = 0, c = 0):

    s = a + b + c
    # print(s)
    return s
r = som(2,3,3)
print(r)
print(som(15,23,15))
rr = som(15,5,6)
rrr = som(15,5)
rrrr = som(15,5)
rrrrr = som(15,5)

print(f'{r} {rr} {rrr} {rrrr} {rrrrr}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num  = int(input('Digite um número:'))

if par(num):
    print('E PAR ! ! !')
else:
    print('E ÍMPAR ! ! !')