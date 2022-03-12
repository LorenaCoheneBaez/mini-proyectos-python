import random

# Reglas:
# * Piedra gana a tijera
# ? Tijera gana a papel
# * Papel gana a piedra


def juego():
    usuario = input("Escoge una opción: piedra, papel o tijera. \n").lower()

    # * Con random.choice podemos pasar opciones que le elegirán al azar
    computadora = random.choice(["piedra", "papel", "tijera"])

    if usuario == computadora:
        return f"¡Empate! Intenta otra vez... \n La computadora eligio: {computadora}"

    if gano_usuario(usuario, computadora):
        return f"¡Muy bien. Ganaste! \n La computadora eligio: {computadora}"

    return f"La computadora eligio: {computadora} \n ¡Perdiste! Juega otra vez..."


def gano_usuario(jugador, eleccion_computadora):
    if ((jugador == "piedra" and eleccion_computadora == "tijera")
        or (jugador == "tijera" and eleccion_computadora == "papel")
            or (jugador == "papel" and eleccion_computadora == "piedra")):
        return True
    else:
        return False


print(juego())
