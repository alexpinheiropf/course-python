# Função enumerate

lista = ["abacate", "bola", "cachorro"]

# Modo que pode-se fazer diferente de enumerate
for i in range(len(lista)):
    print(i, lista[i])

# Utilizando a função enumerate
for i, nome in enumerate(lista):
    print(i, nome)