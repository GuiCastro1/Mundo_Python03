# lista =  {
# nome:'Guilherme',
# idade:25,
# }
# print(lista[nome])
# print(lista[idade])
# lista[sexo] = 'M'
'''
lista = {
    'titulo':'Joyland',
    'ano': 2013,
    'autor':'Stephen King'
}
print(lista.values())# pega JOYLAND 2013 STEPHEN KING
print(lista.keys())# TITULO ANO AUTOR
print(lista.items())# PEGA KEYS E VALUES

for  k, v in lista.items():

    print(f'O {k} é {v}')
# itens 
# chaves
# valor
'''
# br = []
# estado1 = {'uf':'São Paulo', 'num':90}
# estado2 = {'uf':'Rio Grande do Sul', 'num':95}

# br.append(estado1)
# br.append(estado2)

# print(br[0]['uf'])
# print(br[0]['num'])
# print(br[1]['uf'])
# print(br[1]['num'])

br = []
estados = {}
for i in range(1,4):
    estados['uf'] = str(input('Digite o nome do seu estado:'))
    estados['sigla'] = str(input('Digite o sigla:'))
    br.append(estados.copy())

# for i in br:
#     print(i)
#     for k, v in i.items():
#         print(f'O campo {k}, tem valor, {v}')
for i in br:
    
    for v in i.values():
        print(f'{v}', end=' ')
    print()