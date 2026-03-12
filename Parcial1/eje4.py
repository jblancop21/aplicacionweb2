
try:

    numeroa = int(input("ingrese un numero:"))
    numerob = int(input("ingrese otro numero:"))


    resultado = numeroa / numerob
    print("el resultado de la division es:", resultado)
except ValueError:
    print("Error: Debe ingresar numeros enteros.")
except ZeroDivisionError:  
    print("No se puede dividir por cero.")


