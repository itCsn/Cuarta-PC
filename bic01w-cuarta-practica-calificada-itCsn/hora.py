class Hora(object):

    def __init__(self, hora, minutos, segundos):
        
        if not (-1 < hora < 24):
            raise ValueError("El valor de hora debe estar entre 0 y 23")
        
        if not (-1 < minutos < 60):
            raise ValueError("El valor de minutos debe estar entre 0 y 59")

        if not (-1 < segundos < 60):
            raise ValueError("El valor de segundos debe estar entre 0 y 59")
 
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    def actualizar(self, hora, minutos, segundos):
        if not (-1 < hora < 24):
            raise ValueError("El valor de hora debe estar entre 0 y 23")
        
        if not (-1 < minutos < 60):
            raise ValueError("El valor de minutos debe estar entre 0 y 59")

        if not (-1 < segundos < 60):
            raise ValueError("El valor de segundos debe estar entre 0 y 59")
 
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self):
        if self.minutos < 10:
            self.minutos = "0" + str(self.minutos)
        if self.segundos < 10:
            self.segundos = "0" + str(self.segundos)
        if 0 < self.hora < 12:
            if self.hora > 9:
                return f"{self.hora}:{self.minutos}:{self.segundos} AM"
            else:
                return f"0{self.hora}:{self.minutos}:{self.segundos} AM"
        if self.hora == 24 or self.hora == 0:
            self.hora = 12
            return f"{self.hora}:{self.minutos}:{self.segundos} AM"
        if self.hora == 12:
            self.hora = 12
            return f"{self.hora}:{self.minutos}:{self.segundos} PM"
        if self.hora > 12: 
            self.hora -= 12
            return f"0{self.hora}:{self.minutos}:{self.segundos} PM"

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
