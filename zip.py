# zip

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]

# Função responsavel em concatenar listas
for numero,nome in zip(lista1, lista2):
    print(numero, nome)
    