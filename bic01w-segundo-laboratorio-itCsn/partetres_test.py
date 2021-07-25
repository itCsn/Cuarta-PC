import io
import re
import sys
from unittest import TestCase, mock

import partetres


class ParteTresTest(TestCase):

    def setUp(self):
        self.float_pattern = "\d+\.\d+"

    @mock.patch('partetres.input', create=True)
    def test_escenario_uno(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["150000"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        partetres.ejecutar()

        numeros_en_salida = re.findall(self.float_pattern, resultado_test.getvalue().strip())
        self.assertEqual(len(numeros_en_salida), 1)
        self.assertAlmostEqual(float(numeros_en_salida[0]), 0.4411, places=2)

    @mock.patch('partetres.input', create=True)
    def test_escenario_dos(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["300000"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        partetres.ejecutar()

        numeros_en_salida = re.findall(self.float_pattern, resultado_test.getvalue().strip())
        self.assertEqual(len(numeros_en_salida), 1)
        self.assertAlmostEqual(float(numeros_en_salida[0]), 0.2206, places=2)

    @mock.patch('partetres.input', create=True)
    def test_escenario_tres(self, entrada_de_prueba):
        entrada_de_prueba.side_effect = ["10000"]

        resultado_test = io.StringIO()
        sys.stdout = resultado_test

        partetres.ejecutar()

        resultado_esperado = "No es posible pagar la inicial en 36 meses"
        self.assertEqual(resultado_test.getvalue().strip(), resultado_esperado)
