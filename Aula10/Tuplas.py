'''
variavel simples  pode guardar só um item um na memoria
Mc = 'Big-Mac'
variavel compasta pode guardar mais de um item um na memoria. Pode acessar os índices começa no 0
Tuplas São Imutáveis
lanche = ('Big-Mac', 'Batata-Frita', 'Coca-Cola' )
Mostra a tupla inteira
print(lanche)
O índice da Coca
print(lanche[2])
O índice do índice 0 até o 1
print(lanche[:2])
O índice começa no 1 e vai até o fim 
print(lanche[1:])
Mostra o último índice Coca
print(lanche[-1])
Mostra o tamanho da tulpa
print(len(lanche))
percorra a variavel e printa o lanche
for i in lanche:
    print(i)
percorra a variavel e printa o lanche e mostra posiçao
for i in range(0, len(lanche)):

    print(lanche[i])
print('Comi pra caramba')

percorra a variavel e printa o lanche e mostra posiçao com metodo enumerate
for j, i in enumerate(lanche):

    print(f'{j} - {i}')

print(sorted(lanche))
print(lanche)

a = (3, 4, 5)
b = (6, 7, 8)
c = a + b
d = b + a

print(c)
print(c.count(3))
deslocamento? pesquisar
print(c.index(3))
print(d)

aceita tipos != int float str boll 

pessoa = ('gui')
del(pessoa)3
print(pessoa)
'''
lanche = ('Big-Mac', 'Batata-Frita', 'Coca-Cola' )

for j, i in enumerate(lanche):

    print(f'{j} - {i}')