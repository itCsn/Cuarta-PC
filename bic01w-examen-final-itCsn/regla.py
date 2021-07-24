def mostrar_regla(numero_pulgadas, longitud_marca_pulgada):
    aux = longitud_marca_pulgada
    guion = "-"
    for i in range(numero_pulgadas + 1):
        if longitud_marca_pulgada - aux == 0:
            print(f"{guion * longitud_marca_pulgada}")
        else:
            aux = aux -1
            while (longitud_marca_pulgada - aux) > 0:
                mostrar_regla(numero_pulgadas, longitud_marca_pulgada - aux) 
                    
if __name__ == "__main__":
    # mostrar_regla(3, 3)
    mostrar_regla(1, 5)
