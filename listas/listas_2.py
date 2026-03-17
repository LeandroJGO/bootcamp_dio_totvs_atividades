# === Métodos da classe list ===
# .append()
lista = []
lista.append(1)
print(f"1 - {lista}") # 1 - [1]

lista.append("Python")
print(f"2 - {lista}") # 2 - [1, 'Python']

lista.append([30, 40, 50])
print(f"3 - {lista}") # 3 - [1, 'Python', [30, 40, 50]]

# .clear
lista.clear() 
print(f"4 - {lista}") # []

# .copy
lista = [1, 'Python', [30, 40, 50]]
lista2 = lista.copy()

print(f"5 - {lista2}") # 5 - [1, 'Python', [30, 40, 50]]

# .count
cores = ["vermelho", "amarelo", "azul", "verde", "vermelho"]
print(f"6 - {cores.count("vermelho")}") # 6 - 2

# .extend
carros = ["gol", "palio", "onix"]
carros.extend(["camaro", "palio", "furgao"])
print(f"7 - {carros}") # 7 - ['gol', 'palio', 'onix', 'camaro', 'palio', 'furgao']

# .index(<elemeto de uma lista>)
print(f"8 - {carros.index("gol")}") # 8 - 0
print(f"8 - {carros.index("palio")}") # 8 - 1

# .pop(<se deixar sem indice retira o ultimo item da lista>)
carros2 = carros.copy()
print(f"9 - {carros2}") # 9 - ['gol', 'palio', 'onix', 'camaro', 'palio', 'furgao']
print(f"9 - {carros2.pop()}")
print(f"9 - {carros2}") # 9 - ['gol', 'palio', 'onix', 'camaro', 'palio'] 

numeros = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(numeros)
