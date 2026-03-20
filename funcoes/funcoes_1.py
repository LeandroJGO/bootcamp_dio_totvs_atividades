''' Função é um bloco de código identificado por um nome e pode
receber uma lista de parâmetros, esses parâmetros podem ou não
ter valores padrões. Usar funções torna o código mais legível
e possibilita o aproveitamento de código. Programar baseado
em funções, é o mesmo que dizer que estamos programando de 
maneira estruturada.'''

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem() # Olá mundo!
exibir_mensagem_2(nome="Guilherme") # Seja bem vindo Guilherme!
exibir_mensagem_3() # Seja bem vindo Anonimo!
exibir_mensagem_3(nome="Pedro") # Seja bem vindo Pedro!

# Retornando valores com funções
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

def func_3():
    print("Olá Mundo!")


print(calcular_total([10,20,34,76])) # 140
print(retorna_antecessor_e_sucessor(10)) # (9, 11)



