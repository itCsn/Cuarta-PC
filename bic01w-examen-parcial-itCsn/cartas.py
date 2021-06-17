import random


def iniciar():
    # Ingrese la solucion en las lineas subsiguientes
    # INICIO
    lista_baraja_inglesa = []
    def tupla(lista_baraja_inglesa,palo):
        numero = ["Uno", "Dos","Tres", "Cuatro", "Cinco", "Seis","Siete", "Ocho", "Nueve", "Diez",]
        for i in numero:
            tupla = (palo, i)
            lista_baraja_inglesa.append(tupla)
        j = (palo, 'Jota')
        q = (palo, 'Reina')
        k = (palo, 'Rey')
        aS = (palo, 'As')
        lista_baraja_inglesa.append(j)
        lista_baraja_inglesa.append(q)
        lista_baraja_inglesa.append(k)
        lista_baraja_inglesa.append(aS)

    # FIN
        return lista_baraja_inglesa
    
    palos = ['Espadas', 'Corazones', 'Trevol', 'Diamantes']
    for i in palos:
        tupla(lista_baraja_inglesa,i)
   
 
    columna1 = []
    random.shuffle(lista_baraja_inglesa)
    for i in lista_baraja_inglesa[:21]:
        columan1.append(i)
    columna2 = []
    for i in lista
 


    # FIN
    return


if __name__ == "__main__":
    iniciar()
