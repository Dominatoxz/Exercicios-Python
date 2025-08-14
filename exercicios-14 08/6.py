numero = int(input("Digite um numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} não pode ser divisivel por ambos simultaneamente")
if numero % 3 == 0:
    print(f"O numero {numero} é divisivel por 3")
else:
    print(f"O numero {numero} não é divisivel por 3")
if numero % 5 == 0:
    print(f"O numero {numero} é divisivel por 5")
else:
    print(f"O numero {numero} não é divisivel por 5")
