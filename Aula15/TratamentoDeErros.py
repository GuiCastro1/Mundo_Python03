'''
Tratamento de Erros e Exceções

as vezes problema as vezes o problema nam sempre é sintatico podem ser:

Erros de Sintaxe
Erros de Tipo e Valor
Erros Matemáticos
Erros de Entrada/Saída (I/O)
Erros de Importação
Erros de Memória

Principais exceções em Python
Exception – Classe base para todas as exceções.
BaseException – Classe base para exceções internas do Python.
KeyboardInterrupt – Ocorre quando o usuário interrompe a execução com Ctrl + C.
SystemExit – Lançada quando sys.exit() é chamado.
GeneratorExit – Ocorre quando um gerador fecha (close() é chamado).
Erros Comuns
1. Erros de Sintaxe
SyntaxError – Erro de sintaxe no código.
IndentationError – Problema de indentação (espaços/tabs incorretos).
TabError – Mistura de espaços e tabs na indentação.
2. Erros de Tipo e Valor
TypeError – Operação inválida entre tipos incompatíveis.
ValueError – Tipo de dado correto, mas valor inválido.
IndexError – Índice fora do intervalo em listas ou tuplas.
KeyError – Chave inexistente em um dicionário.
AttributeError – Atributo ou método inexistente em um objeto.
NameError – Variável ou nome de função não definido.
UnboundLocalError – Uso de variável local antes de ser definida.
3. Erros Matemáticos
ZeroDivisionError – Divisão por zero.
OverflowError – Número muito grande para ser representado.
FloatingPointError – Erro em operações de ponto flutuante (raro).
4. Erros de Entrada/Saída (I/O)
FileNotFoundError – Arquivo não encontrado.
IOError – Erro genérico de entrada/saída.
PermissionError – Permissão negada ao acessar um arquivo.
IsADirectoryError – Arquivo esperado, mas um diretório foi encontrado.
NotADirectoryError – Diretório esperado, mas um arquivo foi encontrado.
5. Erros de Importação
ImportError – Módulo não encontrado.
ModuleNotFoundError – Subclasse de ImportError, mais específica.
6. Erros de Iteração
StopIteration – Final de um iterador atingido.
StopAsyncIteration – Final de um iterador assíncrono.
7. Erros de Memória
MemoryError – Memória insuficiente para uma operação.
RecursionError – Limite máximo de recursão atingido.
8. Outros Erros
AssertionError – Falha em uma instrução assert.
RuntimeError – Erro genérico de tempo de execução.
NotImplementedError – Método ou função ainda não implementado.
Exemplo de Tratamento de Erros
Aqui está um exemplo de como capturar exceções usando try...except:

python
Copiar
Editar
try:
    x = int(input("Digite um número: "))
    y = 10 / x
except ZeroDivisionError:
    print("Erro: Divisão por zero!")
except ValueError:
    print("Erro: Entrada inválida, digite um número inteiro.")
except Exception as e:
    print(f"Erro inesperado: {e}")
else:
    print(f"Resultado: {y}")
finally:
    print("Fim do programa.")
Se quiser mais detalhes sobre uma exceção específica, me avise! 🚀
'''
x = 'Hello, World ! ! !'
print(x)

'''
Sintax
# try:
#     operação

# except:
#     falhou

else & fanally não são obrogatórias

1 try pode ter varios except
'''

try:

    a = int(input('Digite um número:'))
    b = int(input('Digite outro número:'))
    r = a / b

except (ValueError, TypeError):
    print('Infelizmente tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Infelizmente tivemos não eé possivel dividir um número por 0')
except Exception as Erro:
    print(f'Infelizmente tivemos um problema o ERRO encontrado foi {Erro.__cause__}')

else:
    print(f'O resultado é {r}')

finally:
    print('Volte sempre ! ! !')