from unittest import TestCase

from cuenta import CuentaBancaria


class CuentaTest(TestCase):

    def test_atributos(self):
        mi_cuenta: CuentaBancaria = CuentaBancaria("MICUENTA", 5, 1.0)
        self.assertEqual(mi_cuenta.numero_cuenta, "MICUENTA")
        self.assertEqual(mi_cuenta.saldo, 0.0)
        self.assertEqual(mi_cuenta.tasa_interes, 5)
        self.assertEqual(mi_cuenta.costo_retiro, 1.0)

        self.assertEqual(str(mi_cuenta),
                         "Cuenta: MICUENTA Saldo: 0.0 PEN Tasa de interes: 5% Costo por retiro: 1.0 PEN")

    def test_calcular_interes(self):
        mi_cuenta: CuentaBancaria = CuentaBancaria("", 1, 0)
        self.assertEqual(mi_cuenta.calcular_interes(), 0.0)

        mi_cuenta.saldo = 100
        self.assertEqual(mi_cuenta.calcular_interes(), 1)

        mi_cuenta.pagar_interes()
        self.assertEqual(mi_cuenta.saldo, 101)

    def test_depositar(self):
        mi_cuenta: CuentaBancaria = CuentaBancaria("", 0, 0.0)
        mi_cuenta.depositar(1)
        self.assertEqual(mi_cuenta.saldo, 1)
        mi_cuenta.depositar(1)
        self.assertEqual(mi_cuenta.saldo, 2)

    def test_retirar(self):
        mi_cuenta: CuentaBancaria = CuentaBancaria("", 0, 1.0)
        with self.assertRaises(Exception) as context:
            _ = mi_cuenta.retirar(1)

        self.assertEqual(ValueError, type(context.exception))
        self.assertEqual("El saldo actual es 0.0 PEN. No es posible retirar 1 PEN con un costo de 1.0 PEN",
                         str(context.exception))

        mi_cuenta.saldo = 3
        mi_cuenta.retirar(1)
        self.assertEqual(mi_cuenta.saldo, 1)
