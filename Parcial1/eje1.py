def num_primo():
    num = int(input("Ingrese un número: "))
    if num < 2:
        print(num , "no es un número primo.")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, " no es un número primo.")
            return
    print(num, "es un número primo.")

num_primo()