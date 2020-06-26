minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi",2, 9.89, True]

# Print item lista
print(minha_lista[2])

# Imprimindo todos os itens da lista
for item in minha_lista:
	print(item)

# Verificando o tamanho da lista
tamanho = len(minha_lista)
print(tamanho)

# Adicionando itens
minha_lista.append("limao")
print(minha_lista)

# Verificando se item esta na lista
if 3 in minha_lista2:
	print("3 esta na lista")

# retirando item da lista
del minha_lista[2:]
print(minha_lista)

minha_lista4 = []
minha_lista4.append(57)

print(minha_lista4)

# Ordenar lista
lista = [124,345,72,46,6,7,22,0]

lista.sort(reverse=True)

print(lista)

lista2 = sorted(lista)
print(lista2)

lista.reverse()
print(lista)

