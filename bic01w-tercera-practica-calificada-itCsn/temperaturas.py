TEMPERATURAS_POR_DIA = {}


def ingresar_temperaturas(dia_semana, numero_temperaturas):
    lista_temperaturas = []
    for dia in range(1, numero_temperaturas + 1):
        temperatura = float(input(f"Ingrese temperatura {dia_semana} para el dia Lunes: "))
        lista_temperaturas.append(temperatura)
    TEMPERATURAS_POR_DIA[dia_semana] = lista_temperaturas

    return None




def mostrar_reporte():
    lista_dias = TEMPERATURAS_POR_DIA.keys()
    lista_temperatura = TEMPERATURAS_POR_DIA.values()
    for dia in lista_dias:
        suma = 0
        for temperatura in TEMPERATURAS_POR_DIA[dia]:
            suma += temperatura
        promedio = suma/len(lista_temperatura)
        print("TEMPERATURA PROMEDIO POR DIA") 
        espacios = " "*(12 - len(dia) - 1 - len(str(promedio)))
        print(f"{dia}:{espacios}{promedio}")
        print("")




if __name__ == "__main__":
    ingresar_temperaturas("Lunes", 3)
    ingresar_temperaturas("Martes", 3)
    mostrar_reporte()
