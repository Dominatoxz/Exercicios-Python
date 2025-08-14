numero = int(input("Digite um numero entre 1 e 7: "))
dias = {1: "Domingo", 2: "Segunda", 3: "Terça", 4: "Quarta", 5: "Quinta", 6: "Sexta", 7: "Sabado"}

if numero in dias:
    print(f"O dia da semana é {dias[numero]}")
else:
    print("Esse dia não existe")







