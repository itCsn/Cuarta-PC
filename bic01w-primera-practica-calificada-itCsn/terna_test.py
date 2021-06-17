import io
import sys
from typing import List

import terna
from pruebabase import PruebaBase, obtener_lineas_archivo, obtener_lineas_consola


class TernaTest(PruebaBase):

    def test_mostrar_ternas(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        terna.iniciar()

        resultado_esperado: List[str] = obtener_lineas_archivo("test/ternas_test.txt")
        resultado_actual: List[str] = obtener_lineas_consola(resultado_test)

        self.assertCountEqual(resultado_esperado, resultado_actual)
