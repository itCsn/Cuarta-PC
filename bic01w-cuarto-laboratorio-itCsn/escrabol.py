import math
import random
import unicodedata

PUNTAJE_POR_LETRA = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

VOCALES = 'aeiou'
CONSONANTES = 'bcdfghjklmnpqrstvwxyz'
LETRAS_INICIALES = 7
ARCHIVO_PALABRAS = 'palabras.txt'


# INICIO: Codigo de soporte.

def remover_acentos(palabra_con_acentos):
    return ''.join(letra for letra in unicodedata.normalize('NFD', palabra_con_acentos)
                   if unicodedata.category(letra) != 'Mn')


def cargar_palabras():
    """
    :return: Una lista de cadena de caracteres normalizada, leidas del archivo ARCHIVO_PALABRAS.
    """
    print("Cargando palabras desde archivo...")

    with open(ARCHIVO_PALABRAS, 'r', encoding='utf8') as archivo_diccionario:
        lineas = archivo_diccionario.readlines()

    lista_palabras = [remover_acentos(linea.strip().lower()) for linea in lineas]
    print("  ", len(lista_palabras), "palabras en diccionario.")
    return lista_palabras


def convertir_palabra_a_diccionario(palabra):
    """

    :param palabra: La cadena de caracteres correspondiente a una palabra.
    :return: Un diccionario. Las claves son las letras de palabra, y los valores el numero de ocurrencias de cada letra.
    """
    diccionario = {}
    for letra in palabra:
        diccionario[letra] = diccionario.get(letra, 0) + 1
    return diccionario


# FIN: Codigo de soporte.

def calcular_puntaje_palabra(palabra, letras_disponibles):
    """
    El puntaje por palabra tiene dos partes:
    - La primera parte es la suma de puntajes por letra de acuerdo a los puntajes en PUNTAJE_POR_LETRA.
    - La segunda parte es el maximo valor entre dos posibilidades: [1] o [7 * t - 3 * (letras_disponibles - t)], donde t
    es el tamanio de palabra.

    El puntaje final es el produel producto  de estas dos partes.

    :param palabra: La cadena de caracteres correspondiente a una palabra.
    :param letras_disponibles: El numero de letras que tiene el usuario al iniciar la ronda.
    :return: El puntaje que el usuario recibe luego de formar 'palabra' usando las letras presentes en
        letras_disponibles.
    """
    t = len(palabra)
    segunda_parte_del_puntaje = max(1, 7 * t - 3 * (letras_disponibles - t))
    if not "*" in palabra:
        primera_parte_del_puntaje = 0
        for letra in palabra:
            primera_parte_del_puntaje += PUNTAJE_POR_LETRA
    else:
        lista = list(palabra)
        lista.remove("*")
        primera_parte_del_puntaje = 0
        for letra in lista:
            primera_parte_del_puntaje += PUNTAJE_POR_LETRA[letra]


    return primera_parte_del_puntaje * segunda_parte_del_puntaje 

def mostrar_diccionario_letras(diccionario_letras):
    """
    Muestra en consola las letras contenidas en diccionario_letras.

    :param diccionario_letras: Un diccionario. Las claves son letras, y los valores el numero de ocurrencias de cada
        letra.
    :return:None
    """
    for letra in sorted(diccionario_letras.keys()):
        for _ in range(diccionario_letras[letra]):
            print(letra, end=' ')
    print()


def repartir_letras(numero_letras):
    """
    Dado el numero de letras a repartir, produce un diccionario con letras aleatorias.

    :param numero_letras: Numero de letras a repartir.
    :return: Un diccionario con las letras repartidas. Las claves son letras, y los valores el numero de ocurrencias
        de cada letra.
    """
    diccionario_letras = {}
    vocales = int(math.ceil(numero_letras / 3))
    comodin = {}

    for _ in range(vocales):
        vocal = random.choice(VOCALES)
        diccionario_letras[vocal] = diccionario_letras.get(vocal, 0) + 1

    for _ in range(vocales, numero_letras):
        consonante = random.choice(CONSONANTES)
        diccionario_letras[consonante] = diccionario_letras.get(consonante, 0) + 1

    for vocal_comodin in range(vocales):
        if not vocal_comodin in diccionario_letras.keys():
            comodin[vocal_comodin] = comodin.get(vocal_comodin,0) + 1
    
    diccionario_letras["*"] = 1

    return diccionario_letras


def actualizar_diccionario_letras(diccionario_letras, palabra):
    """
    Los jugadores forman palabras usando las letras en diccionario_letras. Esta funcion produce un nuevo diccionario,
    donde las letras de 'palabra' son removidas de diccionario_letras.

    :param diccionario_letras: Un diccionario con las letras en mano. Las claves son las letras, y los
        valores el numero de ocurrencias de cada letra.
    :param palabra: La cadena de caracteres correspondiente a la palabra ingresada por el usuario.
    :return: Un nuevo diccionario, donde las letras de 'palabra' han sido removidas de diccionario_letras.
    """
    nuevo_diccionario_letras = {} 
    for letra in diccionario_letras.keys():
        nuevo_diccionario_letras[letra] = 1
        if letra in palabra:
            nuevo_diccionario_letras[letra] -= 1

    return nuevo_diccionario_letras


def es_palabra_valida(palabra, diccionario_letras, lista_palabras):
    """
    Determina si 'palabra' es valida de acuerdo a dos criterios:

    - 'palabra' esta dentro de lista_palabras.
    - Es posible formar 'palabra' con las letras de diccionario_letras.

    :param palabra: La cadena de caracteres correspondiente a la palabra ingresada por el usuario.
    :param diccionario_letras: Un diccionario con las letras en mano. Las claves son las letras, y los
        valores el numero de ocurrencias de cada letra.
    :param lista_palabras: Un listado de cadenas de caracteres, conteniendo las palabras permitidas en el juego.
    :return: True en caso sea una palabra valida, False en caso contrario.
    """
    comodin = list(VOCALES)
#    comodin = ["a", "e", "i", "o", "u"]
    if "*" in palabra:
        asterisco_en_palabra = True
    
        if not asterisco_en_palabra:
            if palabra.lower() in lista_palabras:
                for letra in palabra.lower():
                    if letra in diccionario_letras.keys():
                        return True
    
        lista = list(palabra)
        indice = lista.index("*")
    #i = 0
        for i in range(5):  
            lista[indice] = comodin[i]
            if "".join(lista) in lista_palabras:
                return True

    #if asterisco_en_palabra:
     #   while not palabra in lista_palabras:
      #      lista[indice] = comodin[0]
       #     palabra = "".join(lista)
        #    if palabra in lista_palabras:
         #       return True
          #  else:
           #     i += 1
        return False


def contar_letras_disponibles(diccionario_letras):
    """
    Calcula el numero de letras que el usuario tiene en mano.

    :param diccionario_letras: Un diccionario con las letras en mano. Las claves son las letras, y los
        valores el numero de ocurrencias de cada letra.
    :return: Un entero, correspondiente al numero total de letras contenidas en diccionario_letras.
    """
    cantidad_de_letras = 0
    for letra in diccionario_letras.keys():
        cantidad_de_letras += 1 
    return cantidad_de_letras


def jugar_ronda(diccionario_letras, lista_palabras):
    """
    Permite jugar una ronda del juego. Una ronda tiene las siguientes caracteristicas:

    - Se le solicita al usuario ingrese una palabra que pueda ser formada con las letras en diccionario_letras.
    - En caso la palabra ingresada sea valida, se incrementa el puntaje del usuario. Caso contrario, se muestra un
    mensaje de error.
    - Luego de ingresar una palabra, se debe reflejar que letras han sido utilizadas.
    - En caso la palabra ingresada sea !!, termina la ronda.
    - La ronda tambien termina cuando el usuario se queda sin letras.
    - Al final de la ronda, se debe mostrar el puntaje acumulado del usuario.

    :param diccionario_letras: Un diccionario con las letras en mano. Las claves son las letras, y los
        valores el numero de ocurrencias de cada letra.
    :param lista_palabras: Un listado de cadenas de caracteres, conteniendo las palabras permitidas en el juego.
    :return: El puntaje total obtenido durante la ronda.
    """
    puntaje_ronda = 0
    print("letras en mano:" , end = ' ')
    mostrar_diccionario_letras(diccionario_letras) 
    palabra = input('Ingrese una palabra, o "!!" para indicar que ha terminado: ')
    while diccionario_letras and palabra != "!!":
        if palabra != "!!":
            if es_palabra_valida(palabra, diccionario_letras, lista_palabras):
                puntaje_de_palabra = calcular_puntaje_palabra(palabra, contar_letras_disponibles(diccionario_letras))
                print(puntaje_de_palabra)
                puntaje_ronda += puntaje_de_palabra
                diccionario_letras = actualizar_diccionario_letras(diccionario_letras, palabra)
                print("letras en mano:" , end = ' ')
                mostrar_diccionario_letras(diccionario_letras) 
                palabra = input('Ingrese una palabra, o "!!" para indicar que ha terminado: ')
                diccionario_letras = actualizar_diccionario_letras(diccionario_letras, palabra)
            else:
                print("No es una palabra valida. Por favor, ingrese otra palabra.")
                print("letras en mano:" , end = ' ')
                mostrar_diccionario_letras(diccionario_letras) 
                palabra = input('Ingrese una palabra, o "!!" para indicar que ha terminado: ')
    #    if palabra == "!!" or actualizar_diccionario_letras(diccionario_letras):
        else:
            print(puntaje_ronda)
            diccionario_letras = actualizar_diccionario_letras(diccionario_letras, palabra)
            return puntaje_ronda


def reemplazar_letra(diccionario_letras, letra):
    """
    Durante el juego, se le permitira al usuario reemplazar TODAS las ocurrencias de una letra que tiene en mano. La
    nueva letra debe ser seleccionada aleatoriamente, entre las letras no aparecen en diccionario_letras.

    :param diccionario_letras:  Un diccionario con las letras en mano. Las claves son las letras, y los
        valores el numero de ocurrencias de cada letra.
    :param letra: La letra a reemplazar.
    :return: Un nuevo diccionario, donde 'letra' ha sido reemplazada por otra letra que no estaba previamente en
        diccionario_letras.
    """
    copia_diccionario_letras = diccionario_letras
    del(copia_diccionario_letras[letra.lower()])
    lista_letras = list("abcdefghijklmnopqrstuvxyz")
    del(list[letra.lower()])
    nueva_letra = random.choice(lista_palabras)
    copia_diccionario_letras[nueva_letra] = 1
    return copia_diccionario_letras


def iniciar(lista_palabras):
    """
   Inicia un juego de escrabol. Un juego tiene las siguientes caracteristicas:

    - El usuario ingresa el numero de rondas.
    - Durante cada ronda, se le reparte al usuario un numero de letras, seleccionadas aleatoriamente.
    - Durante un juego, los usuarios tiene UNA oportunidad de reemplazar una de las letras que le fueron asignadas.
    - Durante un juego, los usuarios tienen UNA posibilidad de repetir una de las rondas que acaban de jugar, incluyendo
      la misma mano.
    - Luego de repetir una ronda, considerar el puntaje maximo entre las dos rondas jugadas.
    - Al final del juego, mostrar el puntaje acumulado.

    :param lista_palabras: Un listado de cadenas de caracteres, conteniendo las palabras permitidas en el juego.
    :return: Un entero, representando el puntaje acumulado de todas las rondas.
    """
    rondas = int(input("Ingrese el numero de rondas: "))
    puntaje_total = 0
    diccionario_letras = repartir_letras(LETRAS_INICIALES)
    print("letras en mano:" , end = ' ')
    mostrar_diccionario_letras(diccionario_letras) 
    reemplazar_letra = input("Quieres reemplazar una letra? ")
    repetir_ronda = True 
    for i in range(rondas):
        jugar_ronda(diccionario_letras, lista_palabras)
        if reemplazar_letra == si:
            letra_a_reemplazar = input("Que letra quieres reemplazar?")
            reemplazar_letra(diccionario_letras, letra_a_reemplazar)

    print(puntaje_total)


if __name__ == "__main__":
    palabras = cargar_palabras()
    
    iniciar(palabras)
