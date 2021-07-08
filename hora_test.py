from unittest import TestCase

from hora import Hora


class HoraTest(TestCase):

    def test_init(self):
        hora_valida = Hora(1, 2, 3)
        self.assertEqual(hora_valida.hora, 1)
        self.assertEqual(hora_valida.minutos, 2)
        self.assertEqual(hora_valida.segundos, 3)

    def test_actualizar(self):
        hora_valida = Hora(0, 0, 0)
        with self.assertRaises(Exception) as context:
            hora_valida.actualizar(24, 0, 0)
        self.assertEqual(ValueError, type(context.exception))
        self.assertEqual("El valor de hora debe estar entre 0 y 23", str(context.exception))

        with self.assertRaises(Exception) as context:
            hora_valida.actualizar(0, 60, 0)
        self.assertEqual(ValueError, type(context.exception))
        self.assertEqual("El valor de minutos debe estar entre 0 y 59", str(context.exception))

        with self.assertRaises(Exception) as context:
            hora_valida.actualizar(0, 0, 60)
        self.assertEqual(ValueError, type(context.exception))
        self.assertEqual("El valor de segundos debe estar entre 0 y 59", str(context.exception))

        hora_valida.actualizar(1, 2, 3)
        self.assertEqual(hora_valida.hora, 1)
        self.assertEqual(hora_valida.minutos, 2)
        self.assertEqual(hora_valida.segundos, 3)

    def test_str(self):
        hora_valida = Hora(0, 0, 0)
        self.assertEqual("12:00:00 AM", str(hora_valida))

        hora_valida = Hora(1, 2, 3)
        self.assertEqual("01:02:03 AM", str(hora_valida))

        hora_valida = Hora(23, 59, 59)
        self.assertEqual("11:59:59 PM", str(hora_valida))
