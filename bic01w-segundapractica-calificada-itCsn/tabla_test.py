import io
import sys
from typing import List

import tabla
from pruebabase import PruebaBase
from tabla import crear_lista


class TablaTest(PruebaBase):

    def test_crear_lista(self):
        resultado: List[List] = crear_lista(2, 3)
        esperado: List[List] = [[1, 2, 3],
                                [4, 5, 6]]

        self.assertEqual(resultado, esperado)

    def test_mostrar_lista(self):
        lista_a_mostrar: List[List] = [[1, 2, 3],
                                       [4, 5, 6]]

        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        tabla.mostrar_lista(lista_a_mostrar)

        self.assert_over_file(resultado_test, "test/mostrar_lista_test.txt")

    def test_iniciar(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        tabla.iniciar()

        self.assert_over_file(resultado_test, "test/tabla_test.txt")
