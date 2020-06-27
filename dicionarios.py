# Dicionarios

meu_dicionario = {"A":"Ameixa", "B":"Bola", "C":"Cachorro"}
print(meu_dicionario["A"])
print(meu_dicionario)

for chave in meu_dicionario:
    print(chave + ' - ' + meu_dicionario[chave])

# Retorna uma tupla com chave/valor
for i in meu_dicionario.items():
    print(i)

# Retorna os valores 
for i in meu_dicionario.values():
    print(i)

# Retorna os chaves 
for i in meu_dicionario.keys():
    print(i)