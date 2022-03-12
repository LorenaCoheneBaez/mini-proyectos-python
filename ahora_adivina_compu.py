import random


def adivina_numero_compu(x):
    print("##################")
    print("Bienvenid@ a adivina el número")
    print("##################")
    print(f"Piensa un número entre 1 y {x} y deja que la compu lo adivine")
    print("##################")
# Establezco el rango númerico que se va a usar
    numero_minimo = 1
    numero_maximo = x

    es_correcto = ""
    # Si se acierta el N° el usuario ingresará c
    while es_correcto != "c":
        if numero_minimo != numero_maximo:
            prediccion = random.randint(numero_minimo, numero_maximo)
        else:
            prediccion = numero_minimo  # ó N° máximo
        # Le pido al usuario que informe si se acertó

        es_correcto = input(
            f"Mi predicción es {prediccion}. Si es un número más alto ingresa (A), si es un número más bajo ingresa (B). Si la predicción es correcta ingresa (C): ").lower()
        # * metodo lower() convierte la min en mayús

        if es_correcto == "a":
            # Porque el N° que puso el usuario es menor al que dijo la computadora
            numero_maximo = prediccion - 1
        elif es_correcto == "b":
            numero_minimo = prediccion + 1

    print(f"¡Felicidades! La computadora adivino el número: {prediccion}")

adivina_numero_compu(10)
