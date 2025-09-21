def eliminar_medio(pila):
    if not pila:
        return None
    
    dato = len(pila) // 2
    dos = []
    for _ in range(dato):
        dos.append(pila.pop())
    eliminado = pila.pop()
    while dos:
        pila.append(dos.pop())
    return eliminado
pila = [1, 2, 3, 4, 5] 
print("Elemento eliminado:", eliminar_medio(pila))  
print("Pila final:", pila)  