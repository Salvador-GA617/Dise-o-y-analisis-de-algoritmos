def Lista(lista):

    if not lista:
        return 0
    return lista[0] + Lista(lista[1:])

numeros = [17,21,5,43,2,9]
print("Suma:", Lista(numeros))  
