def iniciar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    numeroBinario = input("Ingrese un numero en sistema binario:")
    lista = list(numeroBinario)
    posicion = len(lista) - 1
    equivalente = 0
 
    for i in range(len(lista)):
 
        numero = int(lista[i])
    
        while numero >= 2:
            
            print("El numero ingresado no es valido.")
            numeroBinario = input("Ingrese un numero en sistema binario:")
            lista = list(numeroBinario)
            numero = int(lista[i])
            
        equivalente = equivalente + numero*2**posicion

    print(f"El equivalente en decimal es {equivalente}")
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    iniciar()
