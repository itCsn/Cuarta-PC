class CuentaBancaria(object):

    def __init__(self, numero_cuenta, tasa_interes, costo_retiro):
        
    def calcular_interes(self):
        return 
    
    def depositar(self, monto):
        return 

    def retirar(self, monto):
         
        return 

    def pagar_interes(self):
        return  

    def __str__(self):
        return 



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



