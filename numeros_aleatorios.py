import random

""" Caso queira rodar apenas um valor deve-se colocar 
o comando random.seed(1) """

# Buscar numeros aleatórios em um random
numero = random.randint(0,10)
print(numero)

# Para escolher algum numero dentro de uma lista
lista = [6,45,9]
numero = random.choice(lista)
print(numero)


