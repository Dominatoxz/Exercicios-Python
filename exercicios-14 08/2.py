print("Seja Bem-Vindo")
print("Vamos calcular seu peso ideal!")
altura = float(input("Digite sua altura: "))
sexo = int(input("Qual seu sexo? (1 para homem e 2 para mulher)"))
peso_h = (72.7 * altura) - 58
peso_m = (62.1 * altura) - 44.7
if sexo == 1:
    print(f"Seu peso ideal é {peso_h:.1f}kg")
elif sexo == 2:
    print(f"Seu peso ideal é {peso_m:.1f}kg")
else:
    print("Valor invalido")