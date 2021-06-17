# BICO1: Tercera Práctica

## Primera Pregunta

Implemente un programa para registrar multiples temperaturas, en grados fahrenheit, por cada dia de la semana. Este
programa debe considerar lo siguiente:

1. Las temperaturas por dia deben almacenarse en el diccionario `TEMPERATURAS_POR_DIA`, definido en el ámbito global en
   el módulo `temperaturas.py`. En este diccionario, las claves son cadenas de caracteres, representando los dias de la
   semana. Los valores son **listas de numeros reales**, donde los elementos son las temperaturas tomadas en cada dia.

2. Complete la implementación de la función `ingresar_temperaturas(dia_semana, numero_temperaturas)`
   del módulo `temperaturas.py`. Esta función recibe como parámetros el dia de la semana `dia_semana`, como cadena de
   caracteres, y el número de valores de temperatura que el usuario va a ingresar `numero_temperaturas`. Esta función
   agrega una entrada a `TEMPERATURAS_POR_DIA`, donde la clave es `dia_semana` y el valor es una lista de numeros reales
   **ingresados por el usuario**. Por ejemplo, al ejecutar `ingresar_temperaturas("Lunes", 3)`
   se muestra lo siguiente en consola:

   ```commandline
   Ingrese temperatura 1 para el dia Lunes: 66
   Ingrese temperatura 2 para el dia Lunes: 70
   Ingrese temperatura 3 para el dia Lunes: 74
   ```
   Luego, al realizar `print(TEMPERATURAS_POR_DIA)` se debería mostrar en consola: `{'Lunes': [66.0, 70.0, 74.0]}`.

## Segunda Pregunta

Complete la implementación de la función `mostrar_reporte()` en el módulo `temperaturas.py`. Esta función, dado el
diccionario `TEMPERATURAS_POR_DIA`, muestra un reporte conteniendo la temperatura promedio por cada dia de la semana. El
reporte debe mostrarse en dos columnas, de **15 caracteres de longitud**. Los promedios debe mostrarse **redondeados a
dos decimales**.

Por ejemplo, al ejecutar lo siguiente:

```python
ingresar_temperaturas("Lunes", 3)
ingresar_temperaturas("Martes", 3)
mostrar_reporte()
```

Deberíamos ver lo siguiente en consola:

```commandline
Ingrese temperatura 1 para el dia Lunes: 66
Ingrese temperatura 2 para el dia Lunes: 70
Ingrese temperatura 3 para el dia Lunes: 74
Ingrese temperatura 1 para el dia Martes: 50
Ingrese temperatura 2 para el dia Martes: 56
Ingrese temperatura 3 para el dia Martes: 64
TEMPERATURA PROMEDIO POR DIA
Lunes:         70.0           
Martes:        56.67          
```

## Tercera Pregunta

Implemente un programa para administrar un diccionario de sinónimos. Este programa debe considerar lo siguiente:

1. El diccionario de sinónimos debe almacenarse en el diccionario `DICCIONARIO_SINONIMOS`, definido en el ámbito global
   en el módulo `sinonimos.py`. En este diccionario, las claves son cadenas de caracteres, representando las entradas
   del diccionario. Los valores son una **lista de cadenas de caracteres**, donde los elementos son los sinónimos de
   cada entrada.

2. Complete la implementación de la función `registrar_sinonimo(entrada, sinonimo)` del módulo `sinonimos.py`. Esta
   función recibe como parámetros dos cadenas de caracteres: la entrada al diccionario `entrada` y el
   sinónimo `sinonimo` a registrar para dicha entrada. Esta función agrega `sinonimo` como elemento de la lista asociada
   a la clave `entrada`
   en `DICCIONARIO_SINONIMOS`. Por ejemplo, al ejecutar lo siguiente:

   ```python
    registrar_sinonimo("bucle", "rizo")
    registrar_sinonimo("condicion", "contexto")
    registrar_sinonimo("bucle", "rulo")
    print(DICCIONARIO_SINONIMOS)
   ```

   Deberiamos ver los siguiente en consola: `{'bucle': ['rizo', 'rulo'], 'condicion': ['contexto']}`.

3. Complete la implementación de la función `mostrar_sinonimos(entrada)` en el módulo
   `sinonimos.py`. Esta función muestra los sinónimos asociados a la entrada `entrada`, de acuerdo a lo almacenado
   en `DICCIONARIO_SINONIMOS`. En caso `entrada` se encuentre en `DICCIONARIO_SINONIMOS`, el resultado debe mostrarse
   en **dos columnas de 15 caracteres de longitud**. Caso contrario, debe mostrarse un mensaje de error. Por ejemplo, al
   ejecutar lo siguiente:

   ```python
    registrar_sinonimo("bucle", "rizo")
    registrar_sinonimo("bucle", "rulo")
    mostrar_sinonimos("condicion")
    mostrar_sinonimos("bucle")   
   ```

   Deberiamos ver los siguiente en consola:

   ```commandline
   La entrada 'condicion' no se encuentra en el diccionario.
   BUCLE:         rizo           
                  rulo           
   ```

4. Complete la implementación de la función `mostrar_diccionario()` en el módulo `sinonimos.py`. Esta función, dado el
   diccionario `DICCIONARIO_SINONIMOS`, muestra en consola el numero de entradas en el diccionario y los sinónimos de
   cada entrada, en **dos columnas de 15 caracteres de longitud**. Por ejemplo, al ejecutar lo siguiente:

   ```python
    registrar_sinonimo("bucle", "rizo")
    registrar_sinonimo("condicion", "contexto")
    registrar_sinonimo("bucle", "rulo")
    registrar_sinonimo("bucle", "onda")
    registrar_sinonimo("condicion", "entorno")
    registrar_sinonimo("condicion", "ambiente")

    mostrar_diccionario()
   ```
   
   Deberiamos ver los siguiente en consola:

   ```commandline
   DICCIONARIO DE SINONIMOS (2 entradas)
   
   BUCLE:         rizo           
                  rulo           
                  onda           
   CONDICION:     contexto       
                  entorno        
                  ambiente       
   ```