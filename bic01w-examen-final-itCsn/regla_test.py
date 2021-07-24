import io
import sys

from pruebabase import PruebaBase
from regla import mostrar_regla


class ReglaTest(PruebaBase):

    def test_dos_pulgadas(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        mostrar_regla(2, 4)
        self.assert_over_file(resultado_test, "test/test_dos_pulgadas.txt")

    def test_regla_tres_pulgadas(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        mostrar_regla(3, 3)
        self.assert_over_file(resultado_test, "test/test_tres_pulgadas.txt")

    def test_regla_una_pulgada(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        mostrar_regla(1, 5)
        self.assert_over_file(resultado_test, "test/test_una_pulgada.txt")
