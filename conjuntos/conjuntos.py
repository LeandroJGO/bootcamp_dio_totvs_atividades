'''Um set é uma coleção que não possui objetos repetidos,
usamos sets para representar conjuntos matemáticos ou eliminar
itens duplicados de um iterável.'''

lista = set([1,2,3,1,3,4])
print(f"1 - {lista}") # 1 - {1,2,3,4}
# Obs: Set não garante a ordem, ele já retorna a lista de forma ordenada

''' Conjuntos em python não suportam indexação e nem fatiamento,
caso queira acessar os seus valores é necessário converter o conjunto
para lista.'''

numeros = {1,2,3,2}
numeros = list(numeros)
print(numeros) # [1,2,3]

# Métodos da classe set

# {}.union
conjunto_a = {1,2}
conjunto_b = {3,4}
print(conjunto_a.union(conjunto_b)) # {1,2,3,4}

#{}.intersection
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.intersection(conjunto_b)) # {2,3}

# {}.difference
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}

# {}.symmetric_difference
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}
print(conjunto_a.symmetric_difference(conjunto_b)) # {1,4}

# {}.issubset
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
print(conjunto_a.issubset(conjunto_b)) # True
print(conjunto_b.issubset(conjunto_a)) # False

# {}.issuperset
conjunto_a = {1,2,3}
conjunto_b = {4,1,2,5,6,3}
print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a)) # True

# {}.isdisjoint
conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}
print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False

# {}.add
sorteio = {1,23}
sorteio.add(25)
print(sorteio) # {1, 25, 23}
sorteio.add(42)
print(sorteio) # {1, 42, 25, 23}

