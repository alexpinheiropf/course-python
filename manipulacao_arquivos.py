# Ler um arquivo 
arquivo = open("arquivo.txt")

texto_completo = arquivo.read() # Funcao para abrir arquivos

print(texto_completo)

# Criar um arquivo
w = open("arquivo2.txt", "w") # Criar arquivo

w.write("Esse eh o meu arquivo") # Colocar texto dentro do arquivo

w.close() # Eh importante fechar um arquivo depois de aberto

# Adicionar frase ao arquivo
w = open("arquivo.txt", "a") # Criar arquivo

w.write("Esse eh o meu arquivo\n") # Colocar texto dentro do arquivo

w.close() # Eh importante fechar um arquivo depois de aberto