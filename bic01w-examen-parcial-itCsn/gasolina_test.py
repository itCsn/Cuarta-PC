import io
import sys
from unittest import mock
from unittest.mock import MagicMock

import gasolina
from pruebabase import PruebaBase


class GasolinaTest(PruebaBase):

    @mock.patch('gasolina.input', create=True)
    def test_calcular_consumo(self, input_mock: MagicMock):
        input_mock.side_effect = ["12.8", "287", "10.3", "200", "5", "120", "-1"]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        gasolina.iniciar()

        self.assert_over_file(resultado_test, "test/gasolina_test.txt")
