import io
import sys
from unittest import mock
from unittest.mock import MagicMock

import binario
from pruebabase import PruebaBase


class BinarioTest(PruebaBase):

    @mock.patch('binario.input', create=True)
    def test_convertir_binario(self, input_mock: MagicMock):
        input_mock.side_effect = ["11012", "1101"]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        binario.iniciar()

        self.assert_over_file(resultado_test, "test/convertir_binario_test.txt")
