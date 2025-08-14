print("O que você deseja fazer?")

while True:
    print("\n Escolha uma das opções abaixo:")
    print(
        "\n 1 - Soma de 2 números"
        "\n 2 - Diferença entre 2 números (maior pelo menor)"
        "\n 3 - Produto entre 2 números"
        "\n 4 - Divisão entre 2 números (o denominador não pode ser zero)"
    )
    escolha = int(input())


    if escolha == 1: 
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
        soma = num1 + num2
        print(f"A soma desses numeros é {soma}")
        
    elif escolha == 2:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
        numeros = [num1, num2]
        diferença = max(numeros) - min(numeros)
        print(f"A diferença desses numeros é {diferença}")
        
    elif escolha == 3:
        num1 = 3
        num2 = int(input("Digite outro numero: "))
        produto = num1 * num2
        print(f"O produto desses numeros é {produto}")
        
    elif escolha == 4:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
        divisão = num1 / num2
        if num2 == 0:
            print("Essa conta não pode ser efetuada.")
        else:
            print(f"A divisão desses numeros é {divisão}")
        
    