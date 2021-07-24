def exponenciacion_iterativo(base, exponente):
    
    if base == 0 and exponente == 0:
        raise ValueError ("Cero elevado a la potencia cero es indeterminado.")
    
    if base != 0 and exponente == 0:
        return 1

    numero = base
    for i in range(exponente - 1):
        numero = numero * base
    return numero
    
def exponenciacion_recursivo(base, exponente):
    
    if base == 0 and exponente == 0:
        raise ValueError ("Cero elevado a la potencia cero es indeterminado.")
    elif base != 0 and exponente == 0:
        return 1

    elif exponente == 1:
        return base
    else:
        return base*exponenciacion_recursivo(base, exponente - 1)


if __name__ == "__main__":
    print("Exponenciacion recursiva de 3⁴: ")
    print(exponenciacion_recursivo(3, 4))
    print("Exponenciacion iterativa: ")
    print(exponenciacion_iterativo(3, 4))
#    exponenciacion_iterativo(0, 0)
#    exponenciacion_recursivo(0, 0)
