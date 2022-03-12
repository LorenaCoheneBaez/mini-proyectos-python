import random


def adivina_el_numero(numero):
    print("##################")
    print("Bienvenid@ a adivina el número")
    print("##################")
    print("Debes adivinar el número generado por la computadora")
    print("##################")

    numero_aleatorio = random.randint(1, numero)

    adivinanza = 0

    while adivinanza != numero_aleatorio:
        # * f-string es para usar un parametro dentro de un string (como string interpolation)

        adivinanza = int(input(f"Adivina un número entre 1 y {numero}: "))

        if adivinanza < numero_aleatorio:
            print("Intenta con un N° mayor")
        elif adivinanza > numero_aleatorio:
            print("Intenta con un N° menor")

    print("¡Felicidades adivinaste!")
    print(f"el N° correcto era {numero_aleatorio}")


adivina_el_numero(10)
