'''Um dicionário é um conjunto não-ordenado de pares chave:valor,
onde as chaves são únicas em uma dada instância do dicionário.
Dicionários são delimitados por chaves: {}, e contém uma lista
de pares chave:valor separada por vírgulas.'''

# Exemplo de criação de dicionário
pessoa = {"nome":"Guilherme", "idade":"28"} # primeira forma de criar um dict
pessoa = dict(nome="Guilherme", idade=28) # segunda forma de criar um dict

# Pegando um dicionário existente e atribuindo uma nova chave:valor
pessoa["telefone"] = "129999-9999"
print(pessoa) # {'nome': 'Guilherme', 'idade': 28, 'telefone': '129999-9999'}

'''Acesso aos dados de um dicionário ocorrem através da chave.'''

# Exemplo de acesso aos valores de um dicionário
dados = {"nome": "Guilherme", "idade": 28, "telefone": "129999-9999"}
print(dados["nome"]) # Guilherme
print(dados["idade"]) # 28
print(dados["telefone"]) # 129999-9999
print(dados) # {'nome': 'Guilherme', 'idade': 28, 'telefone': '129999-9999'}

''' Dicionários aninhados: Podem armazenar qualquer tipo de objeto python
como valor, desde que a chave para esse valor seja um objeto imutável como
 (strings e números).'''

# Exemplo de dicionário aninhado
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1299999-9999"},
    "alberto@gmail.com": {"nome":"Alberto", "telefone": "1298888-8888"},
    "roberto@gmail.com": {"nome": "Roberto", "idade": 28, "telefone": "1297777-7777"}
}
print(contatos["roberto@gmail.com"]) # {'nome': 'Roberto', 'idade': 28, 'telefone': '1297777-7777'}
print(contatos["roberto@gmail.com"]["idade"]) # 28
print(contatos["alberto@gmail.com"]["nome"]) # Alberto

# Iterando sobre um dicionário
for chave in contatos:
    print(f"chave: {chave} | valor: {contatos[chave]}")

# Iterando sobre um dicionário utilizando o método .items()
for chave, valor in contatos.items():
    print(f"chave: {chave} | valor: {valor}")


