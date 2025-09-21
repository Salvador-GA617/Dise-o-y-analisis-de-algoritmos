def contar_digitos(n):
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)
num = 123456789
print("Son", contar_digitos(num),"digitos")