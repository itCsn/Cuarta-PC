import string
# INICIO: Codigo de soporte
import unicodedata


def remover_acentos(palabra_con_acentos):
    return ''.join(letra for letra in unicodedata.normalize('NFD', palabra_con_acentos)
                   if unicodedata.category(letra) != 'Mn')


def cargar_diccionario(nombre_archivo):
    """
    :param nombre_archivo: Archivo de texto.
    :return: Una lista de cadena de caracteres, conteniendo las palabras en el archivo
    nombre_archivo.
    """
    print("Cargando diccionario desde archivo...")
    with open(nombre_archivo, 'r', encoding='utf8') as archivo_diccionario:
        lineas = archivo_diccionario.readlines()

    diccionario = [remover_acentos(linea.strip().lower()) for linea in lineas]
    print("  ", len(diccionario), "palabras en diccionario.")
    return diccionario

def esta_en_diccionario(diccionario, palabra):
    """
    Verifica si palabra esta en diccionario, excluyendo espacios en blanco y signos
    de puntuacion.
    :param diccionario: Listado de cadenas de caracteres.
    :param palabra: Cadena de caracteres a verificar.
    :return: True si palabra esta en diccionario. False caso contrario.
    """
    palabra = palabra.lower()
    palabra = palabra.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return palabra in diccionario


def obtener_mensaje_confidencial():
    """
    :return: El contenido del archivo confidencial.txt, como cadena de caracteres.
    """
    archivo = open("confidencial.txt", "r")
    mensaje_confidencial = str(archivo.read())
    archivo.close()
    return mensaje_confidencial


# FIN: Codigo de soporte.

def construir_diccionario_desplazamiento(desplazamiento):
    """
    Genera un diccionario donde, de acuerdo al desplazamiento, las claves son las letras del
    mensaje original y los valores son los valores encriptados de cada letra.

    :param desplazamiento: Numero entero para el desplazamiento.
    :return: Diccionario, con claves para letras mayusculas y minusculas.
    """
    letras = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"
    lista_completa = list(letras)
    diccionario = {}

    for i in lista_completa:
        j = lista_completa.index(i) + 2 * desplazamiento
        if j < 52:
            diccionario[i] = lista_completa[j]
        else:
            j -= 52
            diccionario[i] = lista_completa[j]

    return diccionario


def aplicar_diccionario_encriptado(texto_mensaje, diccionario_encriptado):
    """

    :param texto_mensaje: Cadena de caracteres a encriptar.
    :param diccionario_encriptado: Diccionario para la encriptacion. Las claves son las letras
    original es y los valores las letras encriptadas.
    :return: La cadena texto_mensaje encriptada.
    """
    letras = diccionario_encriptado.keys()
    lista_palabra_encriptada = []
    for i in texto_mensaje:
        if i in letras:
            letra = diccionario_encriptado[i]
            lista_palabra_encriptada.append(letra)
        if i in (" !@#$%^&*()-_+={}[]|\:;'<>?,./\""):
            lista_palabra_encriptada.append(i)
    return "".join(lista_palabra_encriptada)


def probar_desplazamiento(mensaje_encriptado):
    """
    Prueba con valores de desplazamiento desde 1 a 26
    """
    diccionario_con_tuplas = {}
    diccionario_a_revisar = cargar_diccionario("diccionario.txt")
    for candidato_desplazamiento in range(26):
        palabras_en_diccionario = 0
        diccionario_encriptado = construir_diccionario_desplazamiento(26-candidato_desplazamiento)
        palabra = aplicar_diccionario_encriptado(mensaje_encriptado, diccionario_encriptado)
        lista_de_palabra = palabra.split(" ")
        tupla = (candidato_desplazamiento,palabra)
        for i in lista_de_palabra:
            if esta_en_diccionario(diccionario_a_revisar, i) :
                palabras_en_diccionario += 1
        diccionario_con_tuplas[palabras_en_diccionario] = tupla
    return diccionario_con_tuplas

class CodificadorPorDesplazamiento(object):

    def __init__(self, texto_mensaje, desplazamiento):
        """

        :param texto_mensaje: Cadena de caracteres, con el mensaje a encriptar.
        :param desplazamiento: Entero. El desplazamiento para el cifrado Cesar.
        """
        self.texto_mensaje = texto_mensaje
        self.desplazamiento = desplazamiento
       

    def get_desplazamiento(self):
        """
        :return: Entero. El valor del campo desplazamiento
        """
        valor_desplazado = self.desplazamiento
        return valor_desplazado

    def get_diccionario_desplazamiento(self):
        """
        :return: Diccionario. Una copia del campo diccionario_desplazamiento.
        """
        desplazamiento = self.desplazamiento
        copia_diccionario_desplazamiento = self.construir_diccionario_desplazamiento(desplazamiento)
        return copia_diccionario_desplazamiento

    def get_texto_mensaje(self):
        """
        :return: Cadena de caracteres. El valor del campo texto_mensaje.
        """
        mensaje = self.texto_mensaje
        return mensaje

    def get_mensaje_encriptado(self):
        """
        :return: Cadena de caracteres. El valor del campo mensaje_encriptado.
        """
        valor_de_desplazamiento = self.desplazamiento
        mensaje = self.texto_mensaje
        diccionario = construir_diccionario_desplazamiento(valor_de_desplazamiento)
        palabra_encriptada = aplicar_diccionario_encriptado(mensaje,diccionario)
        return palabra_encriptada

    def cambiar_desplazamiento(self, nuevo_desplazamiento):
        """
        Permite actualizar el valor del desplazamiento usado para el Cifrado Cesar.
        :param nuevo_desplazamiento: Nuevo valor del desplazamiento.
        :return: None
        """
        self.desplazamiento = nuevo_desplazamiento
        pass


class DecodificadorPorDesplazamiento(object):

    def __init__(self, mensaje_encriptado):
        """
        :param mensaje_encriptado: Cadena de caracteres, con el mensaje a desencriptar.
        """
        self.mensaje_encriptado = mensaje_encriptado
        pass

    def descifrar_mensaje(self):
        """
        Desencripta mensajes codificados usando el Codigo Cesar. Para esto se realiza lo siguiente:
        - Probamos con 26 valores de desplazamiento.
        - Por cada valor, desencriptamos y contamos cuantas palabras estan en diccionario.txt.
        - Utilizamos el valor de desplazamiento que genere el maximo numero de palabras en diccionario.txt.

        :return: Tupla. El primer elemento es el mejor desplazamiento encontrado, y el segundo elemento es el mensaje
        desencriptado.
        """
        mensaje_encriptado = self.mensaje_encriptado
        diccionario_con_tuplas = probar_desplazamiento(mensaje_encriptado)
        palabras_maxima = max(diccionario_con_tuplas.keys())
        tupla_maxima = diccionario_con_tuplas[palabras_maxima]
        return tupla_maxima

    def get_diccionario(self):
        """
        :return: Una copia del campo diccionario.
        """
        copia_diccionario = cargar_diccionario("diccionario.txt")
        return copia_diccionario


if __name__ == "__main__": 
    mensaje_en_clave = DecodificadorPorDesplazamiento(obtener_mensaje_confidencial())
    print(mensaje_en_clave.descifrar_mensaje())

    decodificador = DecodificadorPorDesplazamiento("Xkxc gn Rgtw!")
    print(decodificador.descifrar_mensaje()) # En consola: (2, 'Viva el Peru!')
    # print(decodificador.get_diccionario())
    codificador = CodificadorPorDesplazamiento("Viva el Peru!", 1)
    print(codificador.get_texto_mensaje()) # En consola: Viva el Peru!
    print(codificador.get_desplazamiento()) # En consola: 1
    print(codificador.get_mensaje_encriptado()) # En consola: Wjwb fm Qfsv!

    codificador.cambiar_desplazamiento(2)
    print(codificador.get_mensaje_encriptado()) # En consola: Xkxc gn Rgtw!
