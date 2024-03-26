numeros = input("Digite os números separados por um espaço: ")

argumentos = numeros.split()

soma = 0

for numero in argumentos:
    if not numero.isdigit():
        print(f"Erro ao somar valores, {numero} é um valor inválido")
    else:
        soma += int(numero)

print(f"A soma dos valores validos é: {soma}")