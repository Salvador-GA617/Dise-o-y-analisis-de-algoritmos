def busqueda_lineal(arreglo, valor):
    comparaciones = 0
    for elemento in arreglo:
        comparaciones += 1
        if elemento == valor:
            return comparaciones  
    return comparaciones  


arreglo = [10, 25, 37, 49, 58, 63, 77, 89]
print("Arreglo:", arreglo)

# Si el valor esta en el arreglo
valor = 49
print(f"Se busca {valor}  Comparaciones realizadas:", busqueda_lineal(arreglo, valor))

# Si el valor no esta en el arreglo
valor = 100
print(f"Se busca {valor}  Comparaciones realizadas:", busqueda_lineal(arreglo, valor))
