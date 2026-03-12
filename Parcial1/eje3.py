def analizartexto():
    texto = input("Ingrese un texto: ")
    letras = len(texto)
    palabras = len(texto.split())
    vocales = sum(1 for letra in texto if letra.lower() in 'aeiou')
    
    print("Total de letras:", letras)
    print("Total de palabras:", palabras)
    print("Total de vocales:", vocales)

analizartexto()