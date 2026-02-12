def cuadrado_y_cubo(n):
    return n**2, n**3

num = int(input("Ingresa un número: "))
cuadrado, cubo = cuadrado_y_cubo(num)
print("cuadrado", cuadrado)
print("cubo", cubo)