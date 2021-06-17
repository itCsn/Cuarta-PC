def generar_lista_booleanos(entero):
    cantidad = entero + 1
    lista = [] 
    for i in range(cantidad):
        lista.append(True)     
        
    return lista

def marcar_como_falso(lista,indice):
    lista[indice] = False
    return lista
 def mostrar_verdaderos(lista):
    #for i in lista:
    #    if i == True:
    #        print(lista.index(i))
    i = 0
    while i in range(len(lista)):
        if lista[i] == True:
            print(i)
        i += 1



def iniciar():
    posibles_primos = generar_lista_booleanos(30)
    for i in range(2,31):
       for j in range(2,31):
           if i != j:
               if i%j == 0:
                   marcar_como_falso(posibles_primos,i)
    marcar_como_falso(posibles_primos,0)
    marcar_como_falso(posibles_primos,1)
    mostrar_verdaderos(posibles_primos)

    pass


if __name__ == "__main__":
    iniciar()
