import io
import sys

import sinonimos
from pruebabase import PruebaBase


class DiccionarioTest(PruebaBase):

    def setUp(self) -> None:
        sinonimos.DICCIONARIO_SINONIMOS = {}

        sinonimos.registrar_sinonimo("bucle", "rizo")
        sinonimos.registrar_sinonimo("bucle", "rulo")
        sinonimos.registrar_sinonimo("bucle", "onda")

        sinonimos.registrar_sinonimo("condicion", "contexto")
        sinonimos.registrar_sinonimo("condicion", "entorno")
        sinonimos.registrar_sinonimo("condicion", "ambiente")

        sinonimos.registrar_sinonimo("valor", "cualidad")
        sinonimos.registrar_sinonimo("valor", "virtud")
        sinonimos.registrar_sinonimo("valor", "capacidad")

    def test_registrar_sinonimo(self):
        self.assertEqual(set(sinonimos.DICCIONARIO_SINONIMOS.keys()), {"bucle", "condicion", "valor"})

        self.assertEqual(set(sinonimos.DICCIONARIO_SINONIMOS["bucle"]), {"rizo", "rulo", "onda"})
        self.assertEqual(set(sinonimos.DICCIONARIO_SINONIMOS["condicion"]), {"contexto", "entorno", "ambiente"})
        self.assertEqual(set(sinonimos.DICCIONARIO_SINONIMOS["valor"]), {"cualidad", "virtud", "capacidad"})

    def test_mostrar_sinonimo_inexistente(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        sinonimos.mostrar_sinonimos("bucles")
        self.assert_over_list(resultado_test, ["La entrada 'bucles' no se encuentra en el diccionario."])

    def test_mostrar_sinonimo(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        sinonimos.mostrar_sinonimos("bucle")
        self.assert_over_file(resultado_test, "test/test_mostrar_sinonimo.txt")

    def test_mostrar_diccionario(self):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test

        sinonimos.mostrar_diccionario()
        self.assert_over_file(resultado_test, "test/test_mostrar_diccionario.txt")
