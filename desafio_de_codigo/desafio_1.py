# Lê a linha de entrada e separa os valores
entrada = input("Insira o valor total e percentual de desconto: ").strip().split()
valor_total = float(entrada[0])
percentual_desconto = int(entrada[1])

def calcula_valor_final(valor_total, percentual_desconto):
  return valor_total - (valor_total*(float(percentual_desconto/100)))

valor_final = calcula_valor_final(valor_total, percentual_desconto)
#print(f"{valor_final:.2f} {percentual_desconto}")
  
# Imprima o valor final com duas casas decimais
print(f"{valor_final:.2f}")