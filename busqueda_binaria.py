# Naive search vs búsqueda binaria
import random
import time


def busqueda_ingenua(lista, target):  # Es el objetivo de la búsqueda
    for i in range(len(lista)):
        if lista[i] == target:
            return i
    # Si no está lo que buscamos en la lista retornamos -1, porque los N° que sí pueden estar son todos positivos.
    return -1


# * Para aplicar búsqueda binaria la lista debe estar ordenada de forma ascendente

# paso o y largo de la lista como limites del intervalo para que busque en toda la lista


def busqueda_binaria(lista, target, limite_inferior_intervalo=None, limite_superior_intervalo=None):
    if limite_inferior_intervalo is None:
        limite_inferior_intervalo = 0
    if limite_superior_intervalo is None:
        limite_superior_intervalo = len(lista)-1
    # No hay intervalo y termina la funcion
    if limite_superior_intervalo < limite_inferior_intervalo:
        return -1

    # * Rescursión

    # * // da un resultado entero
    punto_medio_intervalo = (
        limite_inferior_intervalo + limite_superior_intervalo) // 2  # division entera

    if lista[punto_medio_intervalo] == target:
        return punto_medio_intervalo
    elif target < lista[punto_medio_intervalo]:
        # la lista y el target siempre son los mismos, cambia el intervalo de la búsqueda.
        return busqueda_binaria(lista, target, limite_inferior_intervalo, punto_medio_intervalo - 1)
        # Si llego a este punto el target es mayor al target y descarto lo que está a la dcha
    else:  # En este caso el target es menor al punto medio.
        # Descarto todo lo de la izq
        return busqueda_binaria(lista, target, punto_medio_intervalo + 1, limite_superior_intervalo)


# * funcion privada si importo este módulo no se va a ejecutar fuera de este archivo
if __name__ == '__main__':
    # Creo una lista de 10000 N°
    largo_lista = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < largo_lista:
        # doy un intervalo de -30 mil a 30 mil
        conjunto_inicial.add(random.randint(-3*largo_lista, 3*largo_lista))

    # Ordeno (sorted()) en forma ascendente y convierto el conjunto en una lista (list())
    lista_numerica_ordenada = sorted(list(conjunto_inicial))

    # Tiempo de búsqueda ingenua
    inicio = time.time()  # Nos va a dar el tiempo actual en segundos
    for target in lista_numerica_ordenada:
        busqueda_ingenua(lista_numerica_ordenada, target)
    fin = time.time()
    print(f"Tiempo que tomó la búsqueda ingenua: {fin-inicio} segundos.")

    # Tiempo búsqueda binaria
    inicio = time.time()
    for target in lista_numerica_ordenada:
        busqueda_binaria(lista_numerica_ordenada, target)
    fin = time.time()
    print(f"Tiempo que tomó la búsqueda binaria: {fin-inicio} segundos.")

# da como resultado mucha más eficiencia en segundos en la busqueda binaria