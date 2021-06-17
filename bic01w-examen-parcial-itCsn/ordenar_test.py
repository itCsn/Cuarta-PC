import io
import sys
from unittest import mock
from unittest.mock import MagicMock

import ordenar
from pruebabase import PruebaBase


class OrdenarTest(PruebaBase):

    @mock.patch('ordenar.input', create=True)
    def test_ordenar_numeros(self, input_mock: MagicMock):
        input_mock.side_effect = ["N", "1000", "200", "30", "200", "1000", "*"]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        ordenar.iniciar()

        self.assert_over_file(resultado_test,  "test/ordenar_numeros_test.txt")

    @mock.patch('ordenar.input', create=True)
    def test_ordenar_texto(self, input_mock: MagicMock):
        input_mock.side_effect = ["T", "BIC01", "W", "UNI", "FIIS", "W", "*"]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        ordenar.iniciar()

        self.assert_over_file(resultado_test,  "test/ordenar_texto_test.txt")