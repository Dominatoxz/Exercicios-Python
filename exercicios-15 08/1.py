def contagem(texto, caractere):
    i = 0
    for c in texto:
        if c == caractere:
            i += 1 
    return i

texto = input("Digite uma string: ").lower()
caractere = input("Digite o caractere que deseja contar: ").lower()

print(f"O caractere {caractere} aparece {contagem(texto, caractere)} vezes na string.")