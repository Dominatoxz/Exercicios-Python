def positivos(numeros):
    for numero in numeros:
        if numero > 0:
            return True
        else: 
            return False
    
numeros = [2, 3,2,3,4,5,6,7,7,5,4,34,6,8,9,8,7,5,4]
print(positivos(numeros))
