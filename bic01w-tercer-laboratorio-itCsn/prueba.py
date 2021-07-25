def obtener_solucion_como_cadena(palabra_secreta, letras_seleccionadas):
    """

    :param palabra_secreta: Cadena de caracteres.
    :param letras_seleccionadas: Lista. Contiene letras como cadenas de caracteres.
    :return: Una cadena de caracteres conteniendo letras y guiones bajos (_), en base a si
    las letras en letras_seleccionadas pertenecen a palabra_secreta.
    Las letras pendientes se representan mediante guion bajo + espacio en blanco.
    """
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    lista = []    
    lista[:0] = palabra_secreta

    for letra in lista:
        if  not letra in letras_seleccionadas:
            i = lista.index(letra)
            lista[i] = "_ "
            stgr = "".join(lista) 
    return stgr


letras = input()
letas_lista = []
letras_lista[:0] = letras
print(obtener_solucion_como_cadena("apple",letras_lista)
