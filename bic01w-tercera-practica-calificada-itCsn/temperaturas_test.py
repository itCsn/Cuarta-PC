import io
import sys
from unittest import mock

import temperaturas
from pruebabase import PruebaBase


class TemperaturasTest(PruebaBase):
    def setUp(self) -> None:
        temperaturas.TEMPERATURAS_POR_DIA = {}

    @mock.patch("temperaturas.input", create=True)
    def test_ingresar_temperaturas(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["66", "70", "74"]
        dia_semana: str = "Lunes"

        temperaturas.ingresar_temperaturas(dia_semana, 3)

        self.assertEqual(temperaturas.TEMPERATURAS_POR_DIA, {"Lunes": [66.0, 70.0, 74.0]})

    @mock.patch("temperaturas.input", create=True)
    def test_mostrar_reporte(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["66", "70", "74", "50", "56", "64", "75", "80", "83"]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        temperaturas.ingresar_temperaturas("Lunes", 3)
        temperaturas.ingresar_temperaturas("Martes", 3)
        temperaturas.ingresar_temperaturas("Miercoles", 3)

        self.assertEqual(temperaturas.TEMPERATURAS_POR_DIA, {"Lunes": [66.0, 70.0, 74.0],
                                                            "Martes": [50.0, 56.0, 64.0],
                                                            "Miercoles": [75.0, 80.0, 83.0]})

        temperaturas.mostrar_reporte()
        self.assert_over_file(resultado_test, "test/test_mostrar_reporte.txt")
