class Pedido(object):
    def __init__(self, numero_mesa, nombre_mesero):

        
    def ordenar(self, plato):
       return 


class Cliente(object):

    def __init__(self, numero_mesa):
        
    def hacer_pedido(self, nombre_plato, mesero):
        
    def obtener_nombre_plato(self):
         


class Mesero(object):

    def __init__(self, nombre):
            

    def tomar_orden(self, nombre_plato):
        return

class PlatoDeComida(object):

    def __init__(self, nombre):
        
    def atender_mesa(numero_mesa, mesero, pedidos):
    

if __name__ == "__main__":
    comida_mesa_siete = ["cebiche", "sudado", "arroz con leche"]
    almuerzos = atender_mesa(7, "Tomas", comida_mesa_siete)

    for almuerzo in almuerzos:
        print(almuerzo)
