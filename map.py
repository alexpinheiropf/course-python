# map

def dobro(x):
    return x*2

valor = [1,2,3,4,5]

valor_dobrado = (map(dobro, valor))

# Pode retornar os valores
for i in valor_dobrado:
    print(i)

# Pode retornar como uma lista
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)

