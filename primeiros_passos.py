# -*- coding: utf8 -*-
# Meu Primeiro Programa
print ("Hello world")
print ("Outra mensagem")
print ("Mensagem 3")

"""
	Comentarios de Várias Linhas
"""

print ("Olá Mundo mãe põem !!!")

# Operações matemáticas
print (2 + 2)

# Estruturas Condicionais
x = 1
y = 2

if x > y:
	print('x é maior que y') 
elif x == y:
	print('x é igual ao y')
else:
	print('y é maior que x')

# Laços de repetição
x = 1

# Laço while
while x < 10:
	print(x)
	x += 1

# Laço For
lista = [1,2,3,4,5]
lista2 = ["olá","mundo","!"]
lista3 = [0,"olá","biscoito","bolacha",9.99,True]

for i in lista3:
	print(i)

# Função Range
for i in range(10,20,2):
	print(i) # 10,12,14,16,18

# Objetos
a = "Alex"
b = "Pinheiro"

concatenar = a + ' ' + b

print(concatenar)

tamanhho = len(concatenar)
print(tamanhho)

print(a[0]) # A
print(a[1]) # l
print(a[2]) # e
print(a[3]) # x

print(concatenar[1:]) # lex Pinheiro

print(concatenar.lower()) # minusculo
print(concatenar.upper()) # maiusculo


concatenar2 = a + ' ' + b + "\n"

print(concatenar2.strip()) #remove caracter invalido

minha_string = "O rato roeu a roupa do rei de Roma" 
minha_string = minha_string.split("r") # quebra por virgula
print(minha_string)

# busca = minha_string.find("rei")
# print(minha_string.find("rei")) # 23

# print(minha_string[busca:]) # rei de Roma

# minha_string = minha_string.replace("rei", "rainha")
# print(minha_string)


# Funções
def soma(x,y):
	return x + y

def multiplicacao(x,y):
	return x * y

s = soma(2, 3)
print(s)

m = multiplicacao(3, 4)
print(m)

print(soma(s, m)) #chamando função recursivamente









			