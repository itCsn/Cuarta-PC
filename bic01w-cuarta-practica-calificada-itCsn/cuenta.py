class CuentaBancaria(object):

    def __init__(self, numero_cuenta, tasa_interes, costo_retiro):
        self.numero_cuenta = numero_cuenta
        self.tasa_interes = tasa_interes
        self.saldo = 0 
        self.costo_retiro = costo_retiro
        self.monto = 0
        self.intereses = 0

    def calcular_interes(self):
        tasa_interes =self.tasa_interes
        interes = float(self.saldo * self.tasa_interes/100)
        self.intereses = interes
        return self.intereses

    def depositar(self, monto):
        self.monto = monto
        self.saldo += self.monto
        return self.saldo

    def retirar(self, monto):
         
        self.monto = monto
        self.saldo -= (self.monto + self.costo_retiro)
        saldo_inicial = self.saldo + self.monto + self.costo_retiro
        if self.saldo < 0:
            raise ValueError(f"El saldo actual es {saldo_inicial} PEN. No es posible retirar {monto} PEN con un costo de {self.costo_retiro} PEN.") 
        else:
            return self.saldo

    def pagar_interes(self):
        tasa_interes = self.tasa_interes
        interes = self.saldo * (1 + tasa_interes / 100 )
        return  interes

    def __str__(self):
        return f"Cuenta: {self.numero_cuenta} Saldo: {float(self.saldo)} PEN Tasa de interes: {self.tasa_interes}% Costo por retiro: {self.costo_retiro} PEN." 



if __name__ == "__main__":
   # mi_cuenta = CuentaBancaria("12345", 5, 1.0)
   # print(mi_cuenta)
   # mi_cuenta.depositar(111)
   # print(mi_cuenta)
   # mi_cuenta.retirar(200)
   # mi_cuenta.retirar(10)
   # print(mi_cuenta)
   # print(mi_cuenta.calcular_interes())
   # mi_cuenta.pagar_interes()
    #print(mi_cuenta)
   # mi_cuenta = CuentaBancaria("12345", 5, 1.0)
   # mi_cuenta.depositar(100)
   # print(mi_cuenta.calcular_interes()) # En consola: 5.0   
   mi_cuenta = CuentaBancaria("12345", 5, 1.0)
   mi_cuenta.depositar(100)
   mi_cuenta.pagar_interes()
   print(mi_cuenta) # En consola: Cuenta: 12345 Saldo: 105.0 PEN Tasa de interes: 5% Costo por retiro: 1.0 PEN



