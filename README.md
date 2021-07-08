# BIC01: Cuarta Práctica

## Primera Pregunta

En el archivo `potencia.py`, implemente un programa para elevar numeros enteros a potencias enteras. Este programa debe
contar con dos funciones:

1. La función `exponenciacion_iterativo(base, exponente)` retorna un valor entero, correspondiente a elevar el numero
   entero `base` a la potencia `exponente` de manera **iterativa**.
2. La función `exponenciacion_recursivo(base, exponente)` retorna un valor entero, correspondiente a elevar el numero
   entero `base` a la potencia `exponente` de manera **recursiva**.

Considerar lo siguiente:

* Ambas funciones deben producir los mismos resultados, para los mismos parámetros:

```python
print(exponenciacion_recursivo(3, 4))  # En consola: 81
print(exponenciacion_iterativo(3, 4))  # En consola: 81
```

* Ambas funciones deben soportar valores de `base` **mayores o iguales a cero**.
* Ambas funciones **no deben soportar elevar cero a la potencia cero**. En caso el usuario utilice dichos valores como
  parámetros, lanzar una instancia de `ValueError` con el mensaje *Cero elevado a la potencia cero es indeterminado*.

## Segunda Pregunta

En el archivo `cuenta.py`, implemente un programa para administrar cuentas bancarias. Este programa contiene la
clase `CuentaBancaria`, que tiene los siguientes atributos:

* El campo `numero_cuenta` es una cadena de caracteres, cuyo valor es proporcionado por el usuario al crear una
  instancia.
* El campo `saldo` es un numero real. Todas las instancias tienen un valor inicial de `0.0`
  para este campo.
* El campo `tasa_interes` es un numero entero, cuyo valor es proporcionado por el usuario al crear una instancia.
  Representa la tasa de interes **en porcentaje**.
* El campo `costo_retiro` es un numero real, cuyo valor es proporcionado por el usuario al crear una instancia.
  Represente el costo para el usuario al momento de realizar un
  **retiro de fondos**.

Al utilizar `print` en instancias de `CuentaBancaria`, deben mostrarse en consola los valores de estos campos. Por
ejemplo, al ejecutar `print(CuentaBancaria("12345", 5, 1.0))` se produce lo
siguiente: `Cuenta: 12345 Saldo: 0.0 PEN Tasa de interes: 5% Costo por retiro: 1.0 PEN`.

Además, la clase `CuentaBancaria` tiene los siguientes métodos:

* El método `depositar` tiene el parámetro `monto`, e incrementa el valor del campo `saldo` en ese valor. Por ejemplo:

    ```python
    mi_cuenta = CuentaBancaria("12345", 5, 1.0)
    print(mi_cuenta)  # En consola: Cuenta: 12345 Saldo: 0.0 PEN Tasa de interes: 5% Costo por retiro: 1.0 PEN
    mi_cuenta.depositar(111)
    print(mi_cuenta)  # En consola: Cuenta: 12345 Saldo: 111.0 PEN Tasa de interes: 5% Costo por retiro: 1.0 PEN
    ```

* El método `retirar` tiene el parámetro `monto`, y reduce el valor del campo `saldo` en ese valor
  **incluyendo además el costo por retiro**. En caso no se cuente con saldo suficiente, se debe lanzar la
  excepción `ValueError` con el mensaje *"El saldo actual es (saldo) PEN. No es posible retirar (monto) PEN con un costo
  de (costo retiro) PEN"*. Por ejemplo:

    ```python
    mi_cuenta = CuentaBancaria("12345", 5, 1.0)
    mi_cuenta.depositar(111)
    # mi_cuenta.retirar(200) Error! ValueError: El saldo actual es 111.0 PEN. No es posible retirar 200 PEN con un costo de 1.0 PEN
    mi_cuenta.retirar(10) 
    print(mi_cuenta) # En consola: Cuenta: 12345 Saldo: 100.0 PEN Tasa de interes: 5% Costo por retiro: 1.0 PEN
    ```
* El método `calcular_interes` retorna un numero real, correspondiente al interes a pagar dado el saldo actual y la tasa
  de interes de la cuenta. Por ejemplo:

    ```python
    mi_cuenta = CuentaBancaria("12345", 5, 1.0)
    mi_cuenta.depositar(100)
    print(mi_cuenta.calcular_interes()) # En consola: 5.0   
    ```

* El metodo `pagar_interes` incrementa el saldo de la cuenta con el interes generado. Por ejemplo:

    ```python
    mi_cuenta = CuentaBancaria("12345", 5, 1.0)
    mi_cuenta.depositar(100)
    mi_cuenta.pagar_interes()
    print(mi_cuenta) # En consola: Cuenta: 12345 Saldo: 105.0 PEN Tasa de interes: 5% Costo por retiro: 1.0 PEN

    ```

## Tercera Pregunta

En el archivo `hora.py`, implemente un programa para representar las horas del dia. Este programa contiene la
clase `Hora`, que tiene los siguientes atributos:

* El campo `hora` es un numero entero, cuyo valor es proporcionado al crear una instancia. Los valores de `hora` válidos
  están **entre 0 y 23**. En caso no sea asi, lanzar una excepción
  `ValueError` con el mensaje *El valor de hora debe estar entre 0 y 23*.

* El campo `minutos` es un numero entero, cuyo valor es proporcionado por el usuario al crear una instancia. Los valores
  de `minutos` válidos están **entre 0 y 59**. En caso no sea asi, lanzar una excepción
  `ValueError` con el mensaje *El valor de minutos debe estar entre 0 y 59*.

* El campo `segundos` es un numero entero, cuyo valor es proporcionado por el usuario al crear una instancia. Los
  valores de `segundos` válidos están **entre 0 y 59**. En caso no sea asi, lanzar una excepción
  `ValueError` con el mensaje *El valor de segundos debe estar entre 0 y 59*.

Los usuarios de la clase `Hora` asignan valores de acuerdo al
[sistema horario de 24 horas](https://es.wikipedia.org/wiki/Sistema_horario_de_24_horas). Sin embargo, al
utilizar `print` sobre estas instancias se debe mostrar la hora en
el [sistema horario de 12 horas](https://es.wikipedia.org/wiki/Sistema_horario_de_12_horas). Por ejemplo:

```python
# hora_cena = Hora(25, 30, 1) Error!: ValueError: El valor de hora debe estar entre 0 y 23
hora_cena = Hora(20, 30, 1)
print(hora_cena)  # En consola: 08:30:01 PM

hora_despertar = Hora(6, 0, 0)
print(hora_despertar)  # En consola: 06:00:00 AM
```

Además, la clase `Hora` tiene el método `actualizar` con el que es posible cambiar los valores de los campos `hora`
, `minutos` y `segundos`. En caso los parámetros tengan valores inválidos, lanzar excepciones de acuerdo a lo
especificado anteriormente. Por ejemplo:

```python
hora_despertar = Hora(6, 0, 0)
# hora_despertar.actualizar(7, 70, 0) Error! ValueError: El valor de minutos debe estar entre 0 y 59
hora_despertar.actualizar(7, 0, 0)
print(hora_despertar)  # En consola: 07:00:00 AM
```


  
