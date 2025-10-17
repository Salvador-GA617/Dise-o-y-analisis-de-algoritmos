A = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

max_producto = A[0] * A[1]
num1, num2 = A[0], A[1]

for i in range(len(A)):
    for j in range(i + 1, len(A)):
        producto = A[i] * A[j]
        if producto > max_producto:
            max_producto = producto
            num1, num2 = A[i], A[j]

print(f"El producto máximo es {max_producto}, obtenido con {num1} y {num2}")
