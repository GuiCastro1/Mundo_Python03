'''
Criado por: Gui Castro 

27/01/2025

Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre a média de cada um. E faça com que o usúario consiga ver as notas de cada aluno individualmente
p = [[joas[media]]]
'''
lista = []
aux = []
while True:

    nome = str(input('Digite o nome do aluno:'))
    n1 = int(input('Digite 1ª nota do aluno:'))
    n2 = int(input('Digite 2ª nota do aluno:'))
    media = (n1 + n2) / 2
    lista.append([nome, n1, n2, media])

    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S / N]')).strip().upper()[0]

    if continuar == 'N':
        break

print(lista)
#mostra o bolietim de tidos os alunos 
print('-=' * 30)
print('BOLETIM')
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)

for i, v in enumerate(lista):
    print(f'O aluno {i:<4} chamado, {v[0]:<10} tem a media de {v[3]:>8.2f}')

while True:

    aluno = str(input('Digite o nome do aluno para exibis as notas\n\n[digite 999 para sair]\n\nnome do aluno:'))

    for i, v in enumerate(lista):

        if v[0] == aluno:
            print('-=' * 30)
            print(f'As notos do aluno {aluno} são {v[1]} e {v[2]}')
            print('-=' * 30)

    if aluno == '999':
        break
