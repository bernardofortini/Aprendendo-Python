
# Criamos um contexto, limitando o escopo onde o arquivo está aberto.
# O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
with open("arquivo.txt", "w") as file:
    
    # escrevemos no arquivo
    file.write("Ana, 19 anos\n")
    file.write("Bernardo, 19 anos\n")

    print("Miguel, 8 anos", file=file) #print tbm escreve no arquivo e n é necessario a quebra de linhas.


    # como estamos DENTRO do contexto, verificamos que o arquivo está ABERTO
    # através do atributo booleano 'closed' (file.closed = False)
    print(file.closed)
# como estamos FORA do contexto, o arquivo está FECHADO (file.closed = True)
print(file.closed)

# Podemos abrir o arquivo para leitura
with open("arquivo.txt", "r") as file:
    # lê o arquivo inteiro
    print(file.read())