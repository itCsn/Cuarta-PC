import io
import sys
from unittest import mock
from unittest.mock import MagicMock

import vuelto
from pruebabase import PruebaBase


class VueltoTest(PruebaBase):

    @mock.patch('vuelto.input', create=True)
    def test_hay_vuelto(self, input_mock: MagicMock):
        input_mock.side_effect = ["28"]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        vuelto.iniciar()

        self.assert_over_file(resultado_test, "test/hay_vuelto_test.txt")

    @mock.patch('vuelto.input', create=True)
    def test_no_hay_vuelto(self, input_mock: MagicMock):
        input_mock.side_effect = ["100"]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        vuelto.iniciar()

        self.assert_over_file(resultado_test, "test/no_hay_vuelto_test.txt")

