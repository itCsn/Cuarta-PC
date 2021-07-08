import time
from typing import Callable, Tuple
from unittest import TestCase

from potencia import exponenciacion_iterativo, exponenciacion_recursivo


class PotenciaTest(TestCase):

    def test_exponenciacion_iterativo(self):
        self.assertEqual(1, exponenciacion_iterativo(3, 0))
        self.assertEqual(3, exponenciacion_iterativo(3, 1))
        self.assertEqual(81, exponenciacion_iterativo(3, 4))

        with self.assertRaises(Exception) as context:
            _ = exponenciacion_iterativo(0, 0)
        self.assertEqual(ValueError, type(context.exception))
        self.assertEqual("Cero elevado a la potencia cero es indeterminado", str(context.exception))

    def test_exponenciacion_recursivo(self):
        self.assertEqual(1, exponenciacion_recursivo(3, 0))
        self.assertEqual(3, exponenciacion_recursivo(3, 1))
        self.assertEqual(81, exponenciacion_recursivo(3, 4))

        with self.assertRaises(Exception) as context:
            _ = exponenciacion_recursivo(0, 0)
        self.assertEqual(ValueError, type(context.exception))
        self.assertEqual("Cero elevado a la potencia cero es indeterminado", str(context.exception))

    def test_comparar_funciones(self):
        base: int = 100
        exponente: int = 950

        resultado_iterativo, tiempo_iterativo = time_execution(lambda: exponenciacion_iterativo(base, exponente))
        resultado_recursivo, tiempo_recursivo = time_execution(lambda: exponenciacion_recursivo(base, exponente))

        self.assertEqual(resultado_iterativo, resultado_recursivo)
        self.assertLess(tiempo_iterativo, tiempo_recursivo)


def time_execution(function_to_time: Callable) -> Tuple[int, float]:
    inicio: float = time.time()
    resultado_iterativo = function_to_time()
    fin: float = time.time()

    return resultado_iterativo, fin - inicio
