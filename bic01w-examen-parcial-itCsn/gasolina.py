def iniciar():
    # Ingrese la solucion en las lineas subsiguientes
    # INICIO
    consumo_total = 0
    tramo = 1
    gasolina = float(input(f"Tramo {tramo}: Ingrese la gasolina consumida, en galones (-1 para terminar: "))
    gasolina = round(gasolina, 2)
    print(f"En el tramno {tramo}, el consumo de gasolina fue {gasolina} millas por galon. ")
    consumo_total += gasolina
    while gasolina != -1:
        tramo += 1
        gasolina = float(input(f"Tramo {tramo}: Ingrese la gasolina consumida, en galones (-1 para terminar: "))
        gasolina = round(gasolina, 2)
        consumo_total += gasolina
        consumo_total = round(consumo_total,2)
        print(f"En el tramno {tramo}, el consumo de gasolina fue {gasolina} millas por galon. ")

    print(f"En {tramo} tramos, el consumo de gasolina fue {consumo_total} millas por galon. ")
 
    # FIN
    return


if __name__ == "__main__":
    iniciar()
