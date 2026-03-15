# Atividade para treinar a interpolação de strings

nome = "Francisco"
idade = 28
profissao = "Engenheiro"
saldo = 25.386

dados = {"nome": nome, "idade": idade, "profissao": profissao}

# ==== Utilizacao do % ====
print("1 - Nome: %s | Idade: %d | Profissao: %s" % (nome, idade, profissao))

# ==== Utilizando .format ====
print("2 - Nome: {} | Idade: {} | Profissao: {}".format(nome, idade, profissao))
print("3 - Nome: {nome} | Idade: {idade} | Profissao: {profissao}".format(nome=profissao, idade=idade, profissao=nome))

# Os números (índices), definem a ordem com que o valor da variável é exibida dentro do print
print("4 - Nome: {2} | Idade: {0} | Profissao: {1}".format(nome, idade, profissao))

# Podemos pegar valores de dicionários e colocar dentro do argumento do método .format(), destacando as chaves dentro do print.
print("5 - Nome: {nome} | Idade: {idade} | Profissao: {profissao}".format(**dados))

# ==== Utilizando f string (Maneira mais fácil e manutenível de utilizar em prints) ====
print(f'6 - Nome: {nome} | Idade: {idade} | Profissao: {profissao}')

# Formatando floats dentro da string (utilizei o .2f para determinar a quantidade de casas decimais)
print(f'7 - Nome: {nome} | Idade: {idade} | Profissao: {profissao} | Saldo: {saldo:.2f}')


