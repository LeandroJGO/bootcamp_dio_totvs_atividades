# Listar podem armazenar diversos tipos de dados
lista = [type(10), type("11"), type(12.12), type("Python")]
print(lista)

# Método para acessar os valores de uma lista
frutas = ["maça", "laranja", "banana", "uva", "pera"]
print(frutas[1]) # retorna 'laranja'
print(frutas[-1]) # Retorna 'pera' (último elemento)
print(frutas[0:3]) # Retorna '['maça', 'laranja', 'banana']'

'''Listas aninhadas: Podem armazenar todos os tipos de objetos Python,
portanto podemos ter listas que armazenam outras listas. Com isso 
podemos criar estrutuas bidimensionais (tabelas), e acessar informando
os índices de linha e coluna'''

# Utilizando uma lista para armazenar outra lista
matriz = [
    [1, "A", 2.2],
    ["B", 3, "4"],
    [6, 5.5, "C"]
]

print(matriz[0]) # Retorna a primeira lista da lista 'matriz'
print(matriz[0][0]) # Pega o primeiro item da lista do primeiro item da matriz
print(matriz[0:2]) # Pega do primeiro indice até o indice 2

# Percorrendo listas
carros = ["gol", "corsa", "palio", "camaro"]

for i in carros:
    print(f'i = {i}')

# Pegando indice em lista utilizando iteração
for indice, carro in enumerate(carros):
    print(f"indice: {indice} e item: {carro}")

# Compreensão de listas
"""A compreensão de lista oferece uma sintaxe mais curta quando
você deseja: criar uma nova lista com base nos valores de uma lista
existente (filtro) ou gerar uma nova lista aplicando alguma
modificação nos elementos de uma lista existente."""

numeros = [1, 40, 2, 5, 8, 9, 12, 66, 35, 33, 77, 98]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Utilizando uma versão mais limpa (comprehend)
pares = [numero for numero in numeros if numero % 2 == 0]

