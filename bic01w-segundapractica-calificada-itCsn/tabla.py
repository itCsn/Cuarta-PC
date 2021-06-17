#def mostrar_lista(lista_de_listas):
#    for i in range(len(lista_de_listas))
#    print("lista_de_listas[i]\t")

def crear_lista(filas,columnas):
    """
    fila:int, numeros de listas internas
    columnas:int, cantidad de números de las listas 
    """
    lista_externa = []
    for i in range(filas):
        lista_interna = []
        for i in range(columnas):
            lista_interna.append(i+1)
        lista_externa.append(lista_interna)
 
def iniciar():
    pass


if __name__ == "__main__":
    iniciar()
