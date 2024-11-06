def soma_digitos(numero):
    soma = 0
    for n in numero:
        soma += int(n)
    return soma

numero = input("Digite um número inteiro: ")
print(soma_digitos(numero))