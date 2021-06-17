import io
from typing import List
from unittest import TestCase


class PruebaBase(TestCase):

    def assert_over_file(self, resultado_test: io.StringIO, nombre_archivo: str) -> None:
        resultado_esperado: List[str] = obtener_lineas_archivo(nombre_archivo)
        resultado_actual: List[str] = obtener_lineas_consola(resultado_test)

        self.assertEqual(len(resultado_esperado), len(resultado_actual))
        for linea_esperado, linea_actual in zip(resultado_esperado, resultado_actual):
            self.assertEqual(linea_esperado, linea_actual)


def obtener_lineas_consola(resultado_test: io.StringIO) -> List[str]:
    todas_las_lineas: str = resultado_test.getvalue().strip()
    return [linea.strip() for linea in todas_las_lineas.split("\n")]


def obtener_lineas_archivo(nombre_archivo: str) -> List[str]:
    with open(nombre_archivo) as archivo_test:
        resultado_esperado: List[str] = archivo_test.readlines()

    return [linea.strip() for linea in resultado_esperado]
