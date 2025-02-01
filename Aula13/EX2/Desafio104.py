'''
Criado por: Gui Castro

30/01/2025

Faça um programa que tenha um afunção chamada ficha(), que recebera dois parâmetros opicionais: o nome de um jogador e os gols que ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido imformado corretamente
'''

def ficha(nome='',gol =0):

    if not nome:
        nome = 'Desconhecido'
    
    return (f'O jogador {nome}, fez {gol}')
    

jogador = input('Nome do jogador: ').strip()  # Evita espaços extras

gol = input('Nº de gols: ').strip()  # Remove espaços antes/depois
gol = int(gol) if gol.isdigit() else 0  # Converte apenas se for número

# Chamada da função
print(ficha(jogador, gol))




'''

    def ficha(nome=0,gol =0):

    if nome or gol:
        return (f'O jogador {nome}, fez {gol}')
    else:
        return (f'O jogador (0), fez gols(0)')

print(ficha('joão', 8))
print(ficha('gui'))
print(ficha(4))
print(ficha())
O ChatGPT disse:
ChatGPT
O seu código tem um erro de lógica ao verificar if nome or gol:. Vamos analisar o problema e a correção.

🔍 Erros no Código
O parâmetro nome=0 não faz sentido

O nome de um jogador não deve ser um número.
O padrão correto seria uma string vazia: nome="".
O if nome or gol: não funciona corretamente

Se nome=0, o Python interpreta 0 como falso.
Se gol=0, o Python também interpreta 0 como falso.
Isso pode levar a comportamentos inesperados.
Não há tratamento adequado para valores não informados

Se nome não for passado, deveria assumir "Desconhecido".
Se gol não for passado, deveria assumir 0.
✅ Correção
Definir nome="" e gol=0 como padrão.
Se nome for vazio, substituir por "Desconhecido".
python
Copiar
Editar
def ficha(nome="", gol=0):
    if not nome:
        nome = "Desconhecido"  # Define um nome padrão se não for passado
    
    return f'O jogador {nome} fez {gol} gols'

# Testes
print(ficha('João', 8))     # O jogador João fez 8 gols
print(ficha('Gui'))         # O jogador Gui fez 0 gols
print(ficha(4))             # O jogador 4 fez 0 gols (errado!)
print(ficha())              # O jogador Desconhecido fez 0 gols
🔥 Saída esperada
mathematica
Copiar
Editar
O jogador João fez 8 gols
O jogador Gui fez 0 gols
O jogador 4 fez 0 gols
O jogador Desconhecido fez 0 gols
Agora, a função trata corretamente os casos onde os valores não são passados. 🚀
'''