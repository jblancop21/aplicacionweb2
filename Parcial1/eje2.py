def calcular_presupuesto():

    precioa = int(input("ingrese un precio:"))
    print("Precio 1:", precioa * 0.10)
    preciob = int(input("ingrese otro precio:"))
    print("Precio 2:", preciob * 0.10)
    precioc = int(input("ingrese un tercer precio:"))
    print("Precio 3:", precioc * 0.10)

    precio = (precioa * 0.10) + (preciob * 0.10) + (precioc * 0.10)
    print("El resultado total es:", precio)

calcular_presupuesto()