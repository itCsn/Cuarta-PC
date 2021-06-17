import io
import sys
from typing import List

import primos
from primos import generar_lista_booleanos, marcar_como_falso, es_verdadero
from pruebabase import PruebaBase


class PrimosTest(PruebaBase):

    def test_generar_lista_booleanos(self):
        maximo_candidato: int = 5
        resultado_esperado: List[bool] = [True, True, True, True, True, True]
        resultado_actual: List[bool] = generar_lista_booleanos(maximo_candidato)
        self.assertEqual(resultado_actual, resultado_esperado)

    def test_marcar_como_falso(self):
        lista_booleanos: List[bool] = [False, True, False]
        marcar_como_falso(lista_booleanos, 1)

        for elemento in lista_booleanos:
            self.assertFalse(elemento)

    def test_es_verdadero(self):
        lista_booleanos: List[bool] = [True, False, False]

        self.assertTrue(es_verdadero(lista_booleanos, 0))

        for indice in range(1, len(lista_booleanos)):
            self.assertFalse(es_verdadero(lista_booleanos, indice))

    def test_mostrar_verdaderos(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        primos.iniciar()

        self.assert_over_file(resultado_test, "test/primos_test.txt")

