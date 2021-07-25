import io
import sys
from unittest import TestCase, mock

import parteuno


class ParteUnoTest(TestCase):

    @mock.patch('parteuno.input', create=True)
    def test_escenario_uno(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["1000000", "120000", "0.10"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        parteuno.ejecutar()

        resultado_esperado = "Numero de meses: 183"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)

    @mock.patch('parteuno.input', create=True)
    def test_escenario_dos(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["500000", "80000", "0.15"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        parteuno.ejecutar()

        resultado_esperado = "Numero de meses: 105"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)