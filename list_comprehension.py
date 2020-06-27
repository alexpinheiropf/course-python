x = [1,2,3,4,5]
y = []

# Usando Lista Normal
for i in x:
    y.append(i**2)

print(x)
print(y)

# Usando List comprehension
# [valor_a_passar laço condição]
z = [i**2 for i in x]
print("Usando List comprehension")
print(x)
print(z)

# Irá imprimir apenas os ímpares
w = [i for i in x if i%2==1]
print(w)
