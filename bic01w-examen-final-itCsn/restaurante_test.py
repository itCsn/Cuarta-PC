from unittest import TestCase, mock
from unittest.mock import MagicMock

from restaurante import PlatoDeComida, Mesero, Cliente, Pedido, atender_mesa


class RestauranteTest(TestCase):

    def test_plato_comida(self):
        plato_de_comida = PlatoDeComida("shambar")
        self.assertEqual("shambar", plato_de_comida.nombre)

    def test_mesero(self):
        mesero = Mesero("cesar")
        self.assertEqual(mesero.nombre, "cesar")

        orden = mesero.tomar_orden("seco")
        self.assertEqual(PlatoDeComida, type(orden))
        self.assertEqual("seco", orden.nombre)

    @mock.patch("restaurante.Mesero.tomar_orden")
    def test_cliente(self, tomar_orden_mock: MagicMock):
        cliente = Cliente(1)
        self.assertEqual(1, cliente.numero_mesa)
        self.assertIsNone(cliente.plato)

        plato_ordenado: str = "shambar"
        tomar_orden_mock.return_value = PlatoDeComida(plato_ordenado)
        mesero: Mesero = Mesero("")
        cliente.hacer_pedido(plato_ordenado, mesero)

        tomar_orden_mock.assert_called_with(plato_ordenado)
        self.assertEqual(cliente.plato.nombre, plato_ordenado)
        self.assertEqual(cliente.obtener_nombre_plato(), plato_ordenado)

    def test_almuerzo_str(self):
        almuerzo: Pedido = Pedido(1, "cesar")
        almuerzo.ordenar("carapulcra")

        self.assertEqual(type(almuerzo.cliente), Cliente)
        self.assertEqual(almuerzo.cliente.numero_mesa, 1)
        self.assertEqual(type(almuerzo.mesero), Mesero)
        self.assertEqual(almuerzo.mesero.nombre, "cesar")

        self.assertEqual(str(almuerzo), "El cliente de la mesa 1 ordeno carapulcra y fue atendido por cesar")

    @mock.patch("restaurante.Cliente.hacer_pedido")
    @mock.patch("restaurante.Cliente.obtener_nombre_plato")
    def test_ordernar_almuerzo(self, obtener_nombre_plato_mock: MagicMock, hacer_pedido_mock: MagicMock):
        almuerzo: Pedido = Pedido(1, "cesar")
        plato: str = "carapulcra"
        obtener_nombre_plato_mock.return_value = plato

        almuerzo.ordenar(plato)
        hacer_pedido_mock.assert_called_with(plato, almuerzo.mesero)

        print(almuerzo)
        obtener_nombre_plato_mock.assert_called()

    def test_atender_mesa(self):
        comida_mesa_siete = ["cebiche", "sudado", "arroz con leche"]
        almuerzos = atender_mesa(7, "Tomas", comida_mesa_siete)

        self.assertEqual(len(almuerzos), 3)
        comida_ordenada = []
        for almuerzo in almuerzos:
            self.assertEqual(almuerzo.mesero.nombre, "Tomas")
            self.assertEqual(almuerzo.cliente.numero_mesa, 7)
            comida_ordenada.append(almuerzo.cliente.obtener_nombre_plato())

        self.assertCountEqual(comida_mesa_siete, comida_ordenada)
