numero = input("Digite um numero: ")
if int(numero) > 0:
    soma = sum(int(digito) for digito in numero)
    print(soma)
else:
    print("Valor invalido")
