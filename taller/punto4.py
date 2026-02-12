def es_par(numero):
    return numero % 2 == 0

n1 = int(input("Ingrese el primer número: "))

if es_par(n1):
    print("es par")
else:
    print("es impar")
