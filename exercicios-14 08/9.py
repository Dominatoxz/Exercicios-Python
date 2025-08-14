print("Seja Bem Vindo!")
print("\nQual sera seu pedido? ")
cardapio = {"Cachorro quente": 100, "Bauru simples": 101, "Bauru com ovo": 102, "Hamburguer": 103, "Cheeseburguer": 104, "Suco": 105, "Refrigerante": 106}
codigos = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.70, 105: 2.20, 106: 1.00}
pedido = input()
quantidade = int(input("Quantos você gostaria? "))
if pedido in cardapio:  
        print(f"O seu pedido na quantidade que você escolheu fica {codigos[cardapio[pedido]] * quantidade:.2f}R$")