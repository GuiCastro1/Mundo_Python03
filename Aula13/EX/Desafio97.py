'''
Criado por: Gui Castro

30/01/2025

Faça um programa que tenha una função chamada area, que receba as dimenssões de um retangular (Largura e Altura) e mostre a area do terreno.

# Passei o argumento errado
# area(Largura)
# area(Altura)

'''
def area(Largura, Altura):

    area = largura * altura
    print('-=' * 18)
    print(f'A área de um terreno {largura} x {altura} é {area:.2f}m²')
    print('-=' * 18)


largura = float(input('Digite a largura em (m):'))
altura = float(input('Digite a altura em (m):'))

area(largura, altura)
