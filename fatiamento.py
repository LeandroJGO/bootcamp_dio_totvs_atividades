# Apresentação de técnicas de fatiamento em strings
nome = "Francisco Guanabara Antunes"
telefone = "13978265447"
# Pegando o último caracter da string 
print(nome[-1]) # retorna o caracter 's'

# Espelhamento da string
print(nome[::-1])

# Pegando o nome do meio
print(nome[10:19])

# Pega o último nome
print(nome[-8:])

# Pegando valores e definindo os passos
print(nome[0:10:2])

# Pegando o DD de um telefone
dd = telefone[:2]
estado = {"11": "São Paulo", "12": "Jacarei"}
if dd in estado:
    print(f'DD: {dd} - {estado[dd]}')
else:
    print("Sem estado registrado para o DD!")
