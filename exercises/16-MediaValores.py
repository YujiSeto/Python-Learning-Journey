qtd=0
soma=0
media=0
valor=float(input("Digite um valor: "))

while(valor>0.0):
    soma = soma + valor
    qtd = qtd + 1
    # Entrada de Valores
    valor = float(input("Digite um valor: "))

# Caso Digite um Valor Negativo o Laço Encerra
media = soma / qtd
print("\n Total da Soma: ",soma)
print("\n Quantidade de Valores Digitados: ",qtd)
print("\n Média dos Valores: %.1f"% media)
