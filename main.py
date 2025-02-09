import random


with open("palabras.txt", "r") as palabrasTxt:
    listaPalabras = [line.strip() for line in palabrasTxt.readlines()]
indicePalabra = random.randint(0, len(listaPalabras) - 1)
palabra = listaPalabras[indicePalabra]
adivinado = False
letrasIntroducidas = []
progreso = ["_"] * len(palabra) 
while not adivinado:
    print(" ".join(progreso))  
    letra = input("Introduce una letra: ").lower()
    if letra in letrasIntroducidas:
        print("Ya intentaste esa letra. Prueba otra.")
        continue
    letrasIntroducidas.append(letra)
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                progreso[i] = letra
    else:
        print("Letra incorrecta.")
    if "_" not in progreso:
        adivinado = True

print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
