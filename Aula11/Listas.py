'''
LISTA SÃO MUTÁVEIS


lista = ['bianca','oi']
#ADICIONA NA LISTA
lista.append('ola')#adidiona oi ao final da lista
lista.insert(1,'bianca')# adiciona no indice desejado e move os outros e refaz o indice
print(lista)
#REMOVE DA LISTA
del lista [1]#passa indice
lista.pop(2)#passa indice/ geralmente usado para tirar o ultimo se não passar ultimo
lista.remove('oi')#pasar valor e vai remover o primeiro que achar
print(lista)

#MANIPULA LISTA
valore = list(range(1, 11))
print(valore)
t = [ 23, 23, 45, 67, 76,87,87,45,23,12,43]
print(t)
t.sort()
print(t)
t.sort(reverse=True)
print(t)
'''

# lista = [ 23, 23, 45, 67, 76,87,87,45,23,12,43]
# c = lista [:] # ISSO COPIA A LISTA ENTÃ NÃO CORRE O RISCO DE MUDAR AS DUAS LISTAS
# c[0]= 10000
# print(c)
# print(lista)#PYTHON FA Z LIGAMENTO DE LISTA !!!!! CUIDADO AO ATRIBUIR LISTAS




# for i in range(0,5):
#     lista.append(int(input('Digite um número:')))

# lista.append(98)
# lista.append(54)
# lista.append(10)
# lista.append(87)
# lista.append(3)

# for j, i in enumerate(lista):
#     print(f'na posição {j +1}, encontrei o valor {i}\n')
# print('FIM\n\nO PRGRAMA ACABOU ! ! ! ! !')