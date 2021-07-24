# BIC01: Examen Final

## Primera Pregunta

En el archivo `regla.py`, complete la implementación de la
función `mostrar_regla(numero_pulgadas, longitud_marca_pulgada)`. Esta función muestra en consola
una [regla inglesa](https://es.wikihow.com/leer-una-regla), conteniendo `numero_pulgadas` pulgadas donde la marca para
pulgadas tiene una longitud de `longitud_marca_pulgada` caracteres. Por ejemplo, al ejecutar `mostrar_regla(3, 3)` se ve
lo siguiente en consola:

```commandline
---0
-
--
-
---1
-
--
-
---2
-
--
-
---3
```

Nótese que la longitud de la marca de pulgadas tiene una longitud de 3 caracteres `-`, la marca de media pulgada tiene
una longitud de 2 caracteres `-`, y la de un cuarto de pulgada una longitud de un solo carácter `-`. En una regla
inglesa, la marca de pulgadas tiene la máxima longitud, y las marcas subsiguientes disminuyen en uno, hasta llegar a la
marca mínima de longitud un carácter. Por ejemplo, al invocar `mostrar_regla(1, 5)`:

```commandline
-----0
-
--
-
---
-
--
-
----
-
--
-
---
-
--
-
-----1
```

En este caso, la marca de pulgadas tiene longitud 5, la marca de media pulgada tiene longitud 4, la marca de un cuarto
de pulgada longitud 3, y asi sucesivamente hasta las marcas de longitud uno. **Se requiere que en su implementación
utilice recursividad**.

## Segunda Pregunta

En el archivo `login.py`, cree un programa para administrar usuarios y contraseñas. Esta información debe almacenarse en
el diccionario `BASE_DE_DATOS`, donde la clave es el usuario y el valor es la contraseña. Dicho programa debe tener las
siguientes características:

* La función `crear_usuario()` realiza la creación de usuarios. En esta función, se le solicita al usuario el ingreso de
  su usuario y contraseña para ser almacenados en `BASE_DE_DATOS`. En caso el usuario ya exista, se debe mostrar un
  mensaje de error y solicitar el ingreso de un nuevo usuario. Esta función retorna una cadena de caracteres
  correspondiente al usuario creado, además de mostrar un mensaje de confirmación.

* La función `ingresar()` valida las credenciales ingresadas por el usuario. En caso las credenciales sean correctas, se
  muestra un mensaje de bienvenida y se retorna
  `True`. Caso contrario, se muestra un mensaje de error y se retorna `False`.

* La función `iniciar()` le muestra al usuario las opciones disponibles en el programa:
    * La opción 1 permite crear usuarios mediante la función `crear_usuario()`.
    * La opción 2 permite acceder al sistema mediante la función `ingresar()`.
    * La opción 3 termina el programa, luego de mostrar un mensaje de despedida.
    * En caso cualquier otra opción, mostrar un mensaje de error.

Los mensajes del programa deben tener el siguiente formato:

```commandline
Ingrese (1) para crear usuario
Ingrese (2) para ingresar
Ingrese (3) para salir
Opcion: 4
Opcion invalida!
Opcion: 1
Ingrese su usuario: gareth
Ingrese su clave:southgate
El usuario gareth se creo con exito
Opcion: 1
Ingrese su usuario: gareth
El usuario gareth ya existe!
Ingrese su usuario: raheem
Ingrese su clave:sterling
El usuario raheem se creo con exito
Opcion: 2
Ingrese su usuario: marcus
Ingrese su clave: rashford
Credenciales incorrectas
Opcion: 2
Ingrese su usuario: gareth
Ingrese su clave: southgate
Bienvenido gareth
Opcion: 3
Chau!
```

## Tercera Pregunta

En el archivo `restaurante.py`, cree un programa para administrar pedidos en un restaurante. El programa debe contar con
los siguientes elementos:

* La clase `PlatoDeComida`, representa la comida ordenada por los clientes. Sólo tiene el campo `nombre`, una cadena de
  caracteres proveída por el usuario de la clase.

* La clase `Mesero`, representa al personal que atiende las mesas. Tiene el campo `nombre`, una cadena de caracteres
  proveída por el usuario de la clase.
    * Además, tiene el método `tomar_orden` que tiene como parámetro la cadena de caracteres `nombre_plato`. Este método
      retorna una instancia de
      `PlatoDeComida` con el nombre `nombre_plato`.

* La clase `Cliente` representa a los clientes del restaurante. Tiene dos campos: `plato` es una instancia de
  `PlatoDeComida` e inicialmente tiene el valor de `None`; y `numero_mesa`, un número entero proveído por el usuario de
  la clase.
    * Además, tiene el método `hacer_pedido` que tiene como parámetro la cadena de caracteres `nombre_plato` y `mesero`,
      una instancia de `Mesero`. En este método, se le asigna al campo `plato` el resultado de invocar `tomar_orden`
      en `mesero`.

    * El método `obtener_nombre_plato` retorna una cadena de caracteres, correspondiente al nombre del plato que el
      cliente ha ordenado.

* La clase `Pedido` representa un pedido hecho por un cliente en el restaurante. Tiene dos campos:
  `cliente` es una instancia de `Cliente` y `mesero` es una instancia de `Mesero`. El número de mesa de `cliente` y el
  nombre de `mesero ` son proveídos por el usuario de la clase.
    * Además, tiene el método `ordenar` con el parámetro `plato`, una cadena de caracteres representando el nombre del
      plato ordenado por el cliente. En este método, se invoca al método `hacer_pedido` de la instancia en el
      campo `cliente`.
    * Al invocar `print` sobre instancias de `Pedido`, se debe mostrar el número de mesa, el nombre del mesero, y el
      plato ordenado por el cliente (mediante el método `obtener_nombre_plato`).

* La función `atender_mesa` permite registrar múltiples pedidos por mesa. Recibe como parámetros el número de mesa, el
  nombre del mesero y una lista de cadenas de caracteres, con los platos a ordenar en la mesa. Esta función retorna una
  lista de instancias de `Almuerzo`. Por ejemplo, el siguiente código:

  ```python
    comida_mesa_siete = ["cebiche", "sudado", "arroz con leche"]
    almuerzos = atender_mesa(7, "Tomas", comida_mesa_siete)

    for almuerzo in almuerzos:
        print(almuerzo)
   ```

  Muestra lo siguiente en consola:

    ```commandline
    El cliente de la mesa 7 ordeno cebiche y fue atendido por Tomas
    El cliente de la mesa 7 ordeno sudado y fue atendido por Tomas
    El cliente de la mesa 7 ordeno arroz con leche y fue atendido por Tomas
    ```