def area_rectangulo(base, altura):
    return base * altura

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area = area_rectangulo(base, altura)
print("El área del rectángulo es:", area)