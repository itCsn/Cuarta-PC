def ejecutar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    costoCasa=int(input("Ingrese el costo de la casa: "))
    salarioAnual=int(input("Ingrese su salario anual: "))
    porcentajeDeAhorro=float(input("Ingrese el porcentaje de ahorro mensual: "))
    aumentoSemestral=float(input("Ingrese el porcentaje de aumento semestral: "))
    salarioSemestral=salarioAnual/2
    ahorroMensual=salarioSemestral*porcentajeDeAhorro/6
    costoInicial=costoCasa/4
    tasa=4/1200
    interes=0
    meses=1
    monto=0

    while monto<costoInicial:
        if meses%6==0:
        ahorroMensual=ahorroMensual*aumentoSemestral + ahorroMensual
        ahorro=ahorroMensual+monto
        interes=ahorro*tasa
        monto=ahorro+interes
        meses+=meses

    print(f"Numero de meses: {meses}")
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    ejecutar()
