import io
import sys
from unittest import TestCase, mock

import partedos


class ParteDosTest(TestCase):

    @mock.patch('partedos.input', create=True)
    def test_escenario_uno(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["500000", "120000", "0.05", "0.03"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        partedos.ejecutar()

        resultado_esperado = "Numero de meses: 142"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)

    @mock.patch('partedos.input', create=True)
    def test_escenario_dos(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["800000", "80000", "0.10", "0.03"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        partedos.ejecutar()

        resultado_esperado = "Numero de meses: 159"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)

    @mock.patch('partedos.input', create=True)
    def test_escenario_tres(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["1500000", "75000", "0.05", "0.05"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        partedos.ejecutar()

        resultado_esperado = "Numero de meses: 261"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)