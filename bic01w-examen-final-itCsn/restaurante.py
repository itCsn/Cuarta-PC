class Pedido(object):
    def __init__(self, numero_mesa, nombre_mesero):
        self.cliente = Cliente
        self.mesero = Mesero
        self.nombre_mesero = nombre_mesero
        self.numero_mesa = numero_mesa
        
    def ordenar(self, plato):
       return self.Cliente.hacer_pedido(plato)

    def __str__(self):
        return f"El cliente de la mesa {self.numero_mesa} ordeno {self.Cliente.obtener_nombre_plato} y fue atendido por {self.nombre_mesero}"


class Cliente(object):

    def __init__(self, numero_mesa):
        self.plato = None
        self.numero_mesa = numero_mesa

    def hacer_pedido(self, nombre_plato, mesero):
        plato = self.mesero.tomar_orden(nombre_plato)
        return plato

    def obtener_nombre_plato(self):
        return plato 


class Mesero(object):

    def __init__(self, nombre):
        self.nombre = nombre
        # self.nombre_plato = ""    

    def tomar_orden(self, nombre_plato):
        plato = PlatoDeComida(self.nombre)
        self.nombre_plato = plato.nombre()
        return self.nombre_plato


class PlatoDeComida(object):

    def __init__(self, nombre):
        self.nombre = nombre
        # return self.nombre

def atender_mesa(numero_mesa, mesero, pedidos):
    Nombre_mesero = Mesero(mesero)
    cliente = Cliente(numero_mesa)
    pedido = Pedido(numero_mesa,  Nombre_mesero)
    for nombre_plato in pedidos:
        orden = Nombre_mesero.tomar_orden(nombre_plato)
        plato = PlatoDeComida(orden)
        
     


if __name__ == "__main__":
    comida_mesa_siete = ["cebiche", "sudado", "arroz con leche"]
    almuerzos = atender_mesa(7, "Tomas", comida_mesa_siete)

    for almuerzo in almuerzos:
        print(almuerzo)
