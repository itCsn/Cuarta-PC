DICCIONARIO_SINONIMOS = {}


def registrar_sinonimo(entrada, sinonimo):
    if entrada in DICCIONARIO_SINONIMOS.keys():
        DICCIONARIO_SINONIMOS[entrada].append(sinonimo)
    else:
        lista_sinonimos = []
        lista_sinonimos.append(sinonimo)
        DICCIONARIO_SINONIMOS[entrada] = lista_sinonimos
    return None



def mostrar_diccionario():
    entradas = len(DICCIONARIO_SINONIMOS.keys())
    print(f"DICCIONARIO DE SINONIMOS ({entradas} entradas)")
    for palabra in DICCIONARIO_SINONIMOS.keys():
        mostart_sinonimos(palabra)

        print("")




def mostrar_sinonimos(entrada):
    for i in DICCIONARIO_SINONIMOS[palabra] :
         longitud_primera_columna = " "*(15 - 1 - len(palabra))
         longitud_segunda_columna = " "*(15 - len(i))
         print(f"{palabra}:{longitud_primera_columna}{i}{longitud_segunda_columna}")

    print("")


if __name__ == "__main__":
    registrar_sinonimo("bucle", "rizo")
    registrar_sinonimo("condicion", "contexto")
    registrar_sinonimo("bucle", "rulo")
    registrar_sinonimo("bucle", "onda")
    registrar_sinonimo("condicion", "entorno")
    registrar_sinonimo("condicion", "ambiente")

    mostrar_diccionario()
