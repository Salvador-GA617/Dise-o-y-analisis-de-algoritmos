def busqueda_binaria(arr, val, inicio, fin):
    if inicio == fin:
        return inicio if arr[inicio] > val else inicio + 1
    if inicio > fin:
        return inicio
    
    medio = (inicio + fin) // 2
    if arr[medio] < val:
        return busqueda_binaria(arr, val, medio + 1, fin)
    elif arr[medio] > val:
        return busqueda_binaria(arr, val, inicio, medio - 1)
    return medio

# Lista de prueba
arr = [34, 2, 10, -5, 8, 100, 23]

# Algoritmo Insertion Sort con Búsqueda Binaria
for i in range(1, len(arr)):
    val = arr[i]
    j = i - 1
    pos = busqueda_binaria(arr, val, 0, j)
    
    while j >= pos:
        arr[j + 1] = arr[j]
        j -= 1
    arr[pos] = val

print("Lista ordenada:", arr)