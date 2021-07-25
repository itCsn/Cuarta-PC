import string

from desplazamiento import aplicar_diccionario_encriptado, cargar_diccionario, esta_en_diccionario
from permutacion import obtener_permutaciones

VOCALES_MINUSCULAS = "aeiou"
VOCALES_MAYUSCULAS = "AEIOU"


def construir_diccionario_sustitucion(permutacion_vocales):
    """

    Genera un diccionario donde, de acuerdo permutacion_vocales, las claves son las letras del
    mensaje original y los valores son los valores encriptados de cada letra.
    Solo deben sustituirse las vocales de acuerdo a permutacion_vocales, las consonantes no deben
    ser sustituidas.

    :param permutacion_vocales: Cadena de caracteres, con una permutación de vocales. El orden de las
    vocales en la permutacion define la sustitucion de vocales en el diccionario resultante.
    :return: Diccionario, con claves para letras mayusculas y minusculas.
    """
    abcdario = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    diccionario_letras = {}
    lista_vocales_permutadas = list(permutacion_vocales)
    lista_vocalesi_mayusculas_permutadas = list(permutacion_vocales.upper())
    lista_vocales = list(VOCALES_MINUSCULAS)
    lista_vocales_mayusculas = list(VOCALES_MAYUSCULAS)

    for i in abcdario:
        if i in VOCALES_MINUSCULAS:
            j = lista_vocales.index(i)
            diccionario_letras[i] = lista_vocales_permutadas[j]
        elif i in VOCALES_MAYUSCULAS:
            j = lista_vocales_mayusculas.index(i)
            diccionario_letras[i] = lista_vocalesi_mayusculas_permutadas[j]
        else:
            diccionario_letras[i] = i

    return diccionario_letras


def aplicar_diccionario_sustitucion(texto_mensaje, diccionario_encriptado):
    lista_texto_encriptado = []
    lista_letras_encriptadas = diccionario_encriptado.keys()

    for i in texto_mensaje:
        if i in lista_letras_encriptadas:
            letra = diccionario_encriptado[i]
            lista_texto_encriptado.append(letra)
        if i in (" !@#$%^&*()-_+={}[]|\:;'<>?,./\""):
            lista_texto_encriptado.append(i)
    return "".join(lista_texto_encriptado)


def probar_sustitucion(mensaje_encriptado):
    """
    Prueba con todas las permutaciones de las 5 vocales
    """
    diccionario_con_permutacion = {}
    diccionario_a_revisar = cargar_diccionario("diccionario.txt")
    permutaciones_de_vocales = obtener_permutaciones("aeiou")
    for permutacion in permutaciones_de_vocales:
        palabras_en_diccionario = 0
        diccionario_encriptado = construir_diccionario_sustitucion(permutacion)
        palabra = aplicar_diccionario_sustitucion(mensaje_encriptado, diccionario_encriptado)
        lista_de_palabra = palabra.split(" ")
        tupla_con_permutacion = (permutacion, palabra)
        for i in lista_de_palabra:
            if esta_en_diccionario(diccionario_a_revisar, i) :
                palabras_en_diccionario += 1
        diccionario_con_permutacion[palabras_en_diccionario] = tupla_con_permutacion
    return diccionario_con_permutacion


class CodificadorPorSustitucion(object):

    def __init__(self, texto_mensaje, permutacion_vocales):
        """

        :param texto_mensaje: Cadena de caracteres, con el mensaje a encriptar.
        :param permutacion_vocales: Cadena de caracteres, con la permutacion de vocales para el cifrado por sustitucion.
        """
        self.texto_mensaje = texto_mensaje
        self.permutacion_vocales = permutacion_vocales
        pass

    def get_diccionario_sustitucion(self):
        """

        :return: Diccionario. Una copia del campo diccionario_sustitucion.
        """
        permutacion_vocales = self.permutacion_vocales
        return construir_diccionario_sustitucion(permutacion_vocales)


    def get_texto_mensaje(self):
        """
        :return: Cadena de caracteres. El valor del campo texto_mensaje.
        """
        texto_mensaje = self.texto_mensaje
        return texto_mensaje


    def get_mensaje_encriptado(self):
        """
        :return: Cadena de caracteres. El valor del campo mensaje_encriptado.
        """
        texto_mensaje = self.texto_mensaje
        permutacion_vocales = self.permutacion_vocales
        diccionario = construir_diccionario_sustitucion(permutacion_vocales)
        mensaje_encriptado = aplicar_diccionario_sustitucion(texto_mensaje, diccionario)
        return mensaje_encriptado


class DecodificadorPorSustitucion(object):

    def __init__(self, mensaje_encriptado):
        """
        :param mensaje_encriptado: Cadena de caracteres, con el mensaje a desencriptar.
        """
        self.mensaje_encriptado = mensaje_encriptado
        pass

    def descifrar_mensaje(self):
        """
        Desencripta mensajes codificados usando Cifrado por Sustitución. Para esto se realiza lo siguiente:
        - Probamos con todas las permutaciones de 5 vocales.
        - Por cada valor, desencriptamos y contamos cuantas palabras estan en diccionario.txt.
        - Utilizamos la permutacion que genere el maximo numero de palabras en diccionario.txt.

        :return: Una cadena de caracteres con el mensaje decodificado.
        """
        mensaje_encriptado = self.mensaje_encriptado
        diccionario_con_permutacion = probar_sustitucion(mensaje_encriptado)
        palabra_maxima = max(diccionario_con_permutacion.keys())
        tupla = diccionario_con_permutacion[palabra_maxima]
        mensaje_decodificado = tupla[1]
        permutacion = tupla[0]
        diccionario_sustitucion = construir_diccionario_sustitucion(permutacion)
        self.permutacion = permutacion
        self.mensaje_decodificado = mensaje_decodificado
        self.diccionario_sustitucion = diccionario_sustitucion
        return mensaje_decodificado

    def get_diccionario(self):
        """
        :return: Una copia del campo diccionario.
        """
        return cargar_diccionario("diccionario.txt")


if __name__ == "__main__":
    codificador = CodificadorPorSustitucion("Buenos dias, querido profesor!", "eaiuo")
    print(codificador.get_texto_mensaje())
    print(codificador.get_mensaje_encriptado())

    decodificador = DecodificadorPorSustitucion("Boanus dies, qoaridu prufasur!")
    print(decodificador.descifrar_mensaje()) # En consola: Buenos dias, querido profesor!
