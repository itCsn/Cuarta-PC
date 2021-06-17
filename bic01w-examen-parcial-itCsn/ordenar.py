def iniciar():
    # Ingrese la solucion en las lineas subsiguientes
    # INICIO
    tipo_de_variable = input("Numeros (N) o texto (T)? ")
    lista_numeros = []
    if tipo_de_variable == "N":
        elemento_numerico = input("Ingrese un elemento de la lista (* para terminar): ")
        lista_numeros.append(elemento_numerico)
        while elemento_numerico != "*":
            elemento_numerico = input("Ingrese un elemento de la lista (* para terminar): ")
            lista_numeros.append(elemento_numerico)
        lista_numeros.remove("*") 
        lista_numeros.sort() 
    
    lista_texto = []
    if tipo_de_variable == "T":
        elemento_texto = input("Ingrese un elemento de la lista (* para terminar): ")
        lista_texto.append(elemento_texto)
        while elemento_texto != "*":
            elemento_texto = input("Ingrese un elemento de la lista (* para terminar): ")
            lista_texto.append(elemento_texto)
        lista_texto.remove("*") 
        lista_texto.sort()
   
    print("Valores ingresados: ")
    for i in set(lista_numeros):
        print(f"*) {i}")
    for j in set(lista_texto):
        print(f"*) {j}")


  

    # FIN
    return


if __name__ == "__main__":
    iniciar()
