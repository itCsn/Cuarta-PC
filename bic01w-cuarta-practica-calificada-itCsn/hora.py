class Hora(object):

    def __init__(self, hora, minutos, segundos):
        


    def actualizar(self, hora, minutos, segundos):
        

    def __str__(self):
        

if __name__ == "__main__":
    # hora_cena = Hora(25, 30, 1)
    hora_cena = Hora(20, 30, 1)
    print(hora_cena)

    hora_despertar = Hora(6, 0, 0)
    # hora_despertar.actualizar(7, 70, 0)
    hora_despertar.actualizar(7, 0, 0)
    print(hora_despertar)
    hora_despertar = Hora(0, 0, 0)
    #hora_despertar.actualizar(7, 70, 0) #Error! ValueError: El valor de minutos debe estar entre 0 y 59
   # hora_despertar.actualizar(7, 0, 0)
    print(hora_despertar)  # En consola: 07:00:00 AM
