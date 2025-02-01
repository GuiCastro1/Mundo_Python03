'''
Criado por: Gui Castro

30/01/2025

Escreva uma programa que contenha uma função chamada escreva, que recebe qualquer texto como parâmetro e mostre uma mensagem com tamanho adaptável

EX: oi   
'''
def escreva(txt):

    tamanho = len(txt) + 4
    print('-' * tamanho)
    print(f'  {txt}')
    print('-' * tamanho)

texto = str(input('Digite um texto:'))
escreva(texto)