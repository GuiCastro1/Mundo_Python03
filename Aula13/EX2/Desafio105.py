'''
Criado por: Gui Castro

30/01/2025

Crie uma função que vai funcionar asemelhante a função de input() do python, só que fazendo validação para aceitar apenas valores númericos.
'''
def leiaint(msg):

    ok = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO DIGITE UM NÚMERO VÁLIDO ! ! !')
        if ok:
            break
        return valor

n = leiaint('Digite um número:')
print(f'Você acabou de digitar o número:{n}')
