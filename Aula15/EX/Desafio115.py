'''
Criado por: Gui Castro

01/01/2025

Crie um codigo em pithon que teste sé o site do pudim esta acessivel pelo computador
'''

import requests
try:
    site = requests.get('https://pudim.com')
    if site.status_code >= 200 and site.status_code <= 399:
        print('Passei Aqui')

except requests.exceptions.ConnectionError:
    print('Erro de Conexão')
except requests.exceptions.Timeout:
    print('Tempo de resposta demorado')
except requests.exceptions.RequestException:
    print('Erro')

finally:
    print('Volte Sempre ! ! !')
       