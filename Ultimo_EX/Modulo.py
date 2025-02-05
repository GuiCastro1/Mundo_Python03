def titulo(valor):

    temanho = len(valor) + 4

    print('-'*temanho)
    print(f'  {valor}')
    print('-'*temanho)

def regex(nome=''):

    lista =  ['/',  ':', '*', '?', '"', '<', '>', '|', '@', '#', '$', '%', '&', '¨', 'á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û', 'ç']
    
    nome = nome.strip().upper()

    nome_sem_espaco = nome.replace(' ', '-')

    caracter = []

    for i in lista:
        if i in nome_sem_espaco:
            print(i)
            nome_sem_espaco = nome_sem_espaco.replace(i, '')
            caracter.append(i)

    if caracter:        
        print(f'Caracteres {caracter} inavlido não aceitamos caracteres especiais ou letra com acento')
        return False
        
    else:
        print(f'Nome Aceito: {nome_sem_espaco}')
        return nome_sem_espaco

def arquivo(arquivo):

    from datetime import date

    data = date.today()

    nome = arquivo + '.txt'

    with open(f'{nome}', 'w') as arquivo:
        arquivo.write(f'Arquivo criado em: {data}\n')
        arquivo.write(f'Nomedo arquivo: {nome}\n')
        arquivo.close()

    return nome

def adiciona(nome_do_arquivo):
    
    while True:
        nome = ''
        idade = 0
        nome = str(input('Digite o nome:'))
        idade = int(input('Digite a idade:'))
        with open(nome_do_arquivo, 'a') as arquivo:
            arquivo.write(f'{nome} \t {idade}\n')

        continuar = str(input('Deseja continuar: [S / N]')).upper().strip()[0]

        while continuar not in 'SN':
            continuar = str(input('Deseja continuar: [S / N]')).upper().strip()[0]
            
        if continuar == 'N':
                break
                arquivo.close()

def le_arquivo(arquivo):
    
    from time import sleep

    with open(arquivo,'r')as temanho:

        tteste = temanho.readlines()

        for i in tteste:
            print(i)
            sleep(1)

        temanho.close()