import random
import string
# Uso este import porque solo quiero una variable del archivo
from palabras_para_ahorcado import palabras
from diagrama_vidas import vidas_diccionario_visual

# diagrama_vidas


# Paso por parametro la lista de palabras
def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():
    print("*********************************")
    print("Bienvenid@ vamos a jugar al ahorcado")
    print("*********************************")

    palabra = obtener_palabra_valida(palabras)

# Establezco 3 conjuntos de letras (por ser conjunto no se repiten las letras)
    # Tiene todas las letras menos la ñ
    abecedario = set(string.ascii_uppercase)

    letras_por_adivinar = set(palabra)

    letras_adivinadas = set()

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas")
        if vidas < 7:
            print(f"Ya has elegido estas letras: {' '.join(letras_adivinadas)}")

    # Acá muestro la letra en la palabra si ya se adivino, y un guion si queda por adivinar
        # * sintaxis de list comprehension
        palabra_lista = [
            letra if letra in letras_adivinadas else '-' for letra in palabra]
        # Diagrama del ahorcado
        print(vidas_diccionario_visual[vidas])
        # la palabra con las letras adivinadas y los espacios por adivinar
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_ingresada_usuario = input("Elige una letra: ").upper()

        # Agrego la letra ingresada si está en el abecedario pero no está en las adivinadas previamente.
        # Puedo restar las letras porque pertenecen a conjuntos
        if letra_ingresada_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_ingresada_usuario)
        # Si la letra ingresada está en la palabra (letras_por_adivinar) saco la letra (ya se adivinó)
        # Puedo usar remove() en conjuntos
        # Si no está en la palabra, resto una vida
            if letra_ingresada_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_ingresada_usuario)
                print(' ')
            else:
                vidas -= 1
                print(
                    f"\nLa letra {letra_ingresada_usuario} que elegiste no está en la palabra. \n Intenta otra vez.")
        # Si la letra ya se había ingresado
        elif letra_ingresada_usuario in letras_adivinadas:
            print("\nYa habías ingresado esa letra... \n Intenta otra vez.")
        else:
            print(
                f"\nEsta letra {letra_ingresada_usuario} no es válida. \n Intenta otra vez.")

    # Llegamos hasta acá al adivinar todas las letras o perder todas las vidas
    if vidas == 0:
            print(vidas_diccionario_visual[vidas])
            print(f"\n ¡¡¡Perdiste!!! \n La palabra era: {palabra}")
    else:
            print(f"\n ¡¡¡Felicidades, adivinaste!!! \n La palabra era {palabra}")


ahorcado()
