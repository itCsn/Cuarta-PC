import io
import sys
from unittest import mock
from unittest.mock import MagicMock

import login
from pruebabase import PruebaBase


class LoginTest(PruebaBase):

    def setUp(self) -> None:
        login.BASE_DE_DATOS = {"pepe": "luna"}

    @mock.patch("login.input", create=True)
    def test_crear_usuario(self, entrada_de_prueba: MagicMock):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test
        entrada_de_prueba.side_effect = ["pepe", "jose", "gabriel"]

        usuario_creado: str = login.crear_usuario()

        self.assert_over_list(resultado_test, ["El usuario pepe ya existe!", "El usuario jose se creo con exito"])
        self.assertTrue("jose" in login.BASE_DE_DATOS.keys())
        self.assertEqual(login.BASE_DE_DATOS["jose"], "gabriel")
        self.assertEqual("jose", usuario_creado)

    @mock.patch("login.input", create=True)
    def test_ingresar_exito(self, entrada_de_prueba: MagicMock):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test
        entrada_de_prueba.side_effect = ["pepe", "luna"]

        exito: bool = login.ingresar()

        self.assertTrue(exito)
        self.assert_over_list(resultado_test, ["Bienvenido pepe"])

    @mock.patch("login.input", create=True)
    def test_iniciar(self, entrada_de_prueba: MagicMock):
        resultado_test: io.StringIO = io.StringIO()
        sys.stdout = resultado_test
        entrada_de_prueba.side_effect = ["4", "1", "simon", "bolivar", "2", "simon", "bolivar", "3"]

        login.iniciar()

        self.assertTrue("simon" in login.BASE_DE_DATOS.keys())
        self.assert_over_file(resultado_test, "test/test_login.txt")
