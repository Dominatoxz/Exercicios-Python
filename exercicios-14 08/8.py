print("Vamos analisar o quão economico seu carro é!")

km = int(input("Quantos kilometros você andou? "))
litros = int(input("Quantos litros seu carro gastou? "))
consumo = km / litros
print(f"O consumo do seu carro é {consumo:.1f}km/L")

if consumo < 8:
    print("Venda seu carro urgentemente!!!!")
elif consumo >= 8 and consumo <= 12:
    print("Seu carro é economico!!")
elif consumo > 12:
    print("Seu carro é muito economico!!!")
