def merge_sort(arr):
    
    if len(arr) > 1:

        mitad = len(arr) // 2
        
        mitad_izquierda = arr[:mitad]
        mitad_derecha = arr[mitad:]

        
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        
        merge(arr, mitad_izquierda, mitad_derecha)

def merge(arr, izq, der):
    
    i = 0 
    j = 0  
    k = 0  

    
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1
        k += 1

    
    while i < len(izq):
        arr[k] = izq[i]
        i += 1
        k += 1

    
    while j < len(der):
        arr[k] = der[j]
        j += 1
        k += 1


arreglo = [38, 27, 43, 3, 9, 82, 10, 1, 5, 99]
print(f"Arreglo original: {arreglo}")

merge_sort(arreglo)

print(f"Arreglo ordenado: {arreglo}")