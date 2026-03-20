# Métodos da classe dict

# Método .clear() (Limpa todas as informações de um dicionário)
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "33333-3333"},
    "alberto@gmail.com": {"nome": "Alberto", "telefone": "44444-4444"},
    "joao@gmail.com": {"nome": "Joao", "telefone": "55555-5555"},
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "66666-6666"}
}
contatos.clear()
print(contatos) # {}

# Médodo .copy (Cria uma cópia de um dicionário)
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "33333-3333"}}
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}
print(contatos["guilherme@gmail.com"]) # {'nome': 'Guilherme', 'telefone': '33333-3333'}
print(copia["guilherme@gmail.com"]) # {'nome': 'Gui'}

carro = {"marca": "Fiat", "modelo": "palio", "placa": "1234"}
print(carro.get("motor"))


