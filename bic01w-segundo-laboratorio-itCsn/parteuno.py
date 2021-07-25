def ejecutar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    costoCasa=int(input("Ingrese el costo de la casa: "))
    salarioAnual=int(input("Ingrese su salario anual: "))
    porcentajeDeAhorro=float(input("Ingrese el porcentaje de ahorro mensual: "))
    ahorroMensual=salarioAnual*porcentajeDeAhorro/12
    costoInicial=costoCasa/4
    tasa=4/1200
    interes=0
    meses=1
    monto=0
    while monto<costoInicial:
        ahorro=ahorroMensual+monto
        interes=ahorro*tasa
        monto=ahorro + interes
        meses+=meses

    print(f"Numero de meses: {meses}")
    # FIN
    return

# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    ejecutar()
