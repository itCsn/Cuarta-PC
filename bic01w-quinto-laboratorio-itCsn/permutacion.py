def obtener_permutaciones(cadena):
    """
    Genera todas las permutaciones diferentes para una cadena de caracteres,
    de manera RECURSIVA.

    :param cadena:Una cadena de caracteres. Puede tener caracteres repetidos.
    :return: Una lista de cadena de caracteres diferentes. Contiene TODAS las permutaciones
    DIFERENTES de la cadena pasada como parametro.
    """

    lista_auxiliar = []

    if len(cadena) == 1:
        lista_auxiliar.append(cadena)
        return lista_auxiliar
    else:
        for i in cadena:
            #str.replace(old, new, count(optional))
            #returns a copy of the string where all occurrences of a substring are replaced with another substring.
            for j in obtener_permutaciones(cadena.replace(i,'',1)):
                lista_auxiliar.append(i + j)
    return sorted(list(set(lista_auxiliar)))

if __name__ == "__main__":
    print(obtener_permutaciones("abcb"))
