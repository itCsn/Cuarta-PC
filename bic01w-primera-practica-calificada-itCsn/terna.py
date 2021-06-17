def iniciar():
    # Ingrese la solucion en las lineas subsiguientes.
    # INICIO
    
    for b in range(1,21):
        for a in range(1,21):
            for c in range(1,21):
                if a**2 == b**2 + c**2 and a>b>c:
                    print(f"({c}, {b}, {a})")
                
    # FIN
    return


# IMPORTANTE! No modificar de esta linea en adelante.
if __name__ == "__main__":
    iniciar()
