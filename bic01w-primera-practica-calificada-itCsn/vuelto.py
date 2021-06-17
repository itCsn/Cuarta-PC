def iniciar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    precioCentimos = float(input("Ingrese el precio en centimos: "))
    pagoCliente = 100
    vuelto = pagoCliente - precioCentimos
 
    monedas25 = vuelto//25
    vuelto = vuelto - monedas25*25
 
    monedas10 = vuelto//10
    vuelto = vuelto - monedas10*10

    monedas5 = vuelto//5
    vuelto = vuelto - monedas5*5

    monedas1 = vuelto

    if monedas25 > 0:
        print(f"{monedas25} monedas de 25 centimos")
    if monedas10 > 0:
        print(f"{monedas10} monedas de 10 centimos")
    if monedas5 > 0:
        print(f"{monedas5} monedas de 5 centimos")
    if monedas1 > 0:
        print(f"{monedas1} monedas de 1 centimos")
        
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    iniciar()
