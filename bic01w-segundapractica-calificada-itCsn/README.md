# BIC01: Segunda Práctica

## Primera Pregunta

En la segunda pregunta, se requiere implementar un programa que genere numeros primos. Este programa **tiene** que
hacer uso de las siguientes funciones, que usted debe definir en el archivo `primos.py`:

1. La función `generar_lista_booleanos` recibe como parámetro el numero entero `indice_maximo`, y retorna una lista de
   booleanos. En esta lista, **todos** los elementos son `True` con índices que van desde `0` hasta `indice_maximo`.

   ```python
   print(generar_lista_booleanos(3)) # En consola: [True, True, True, True]
   ```
2. La función `marcar_como_falso` recibe como parámetros la lista `lista_booleanos` y el entero `indice`. Esta función
   asigna el valor de `False` al elemento de índice `indice` en `lista_booleanos`.

   ```python
    lista = generar_lista_booleanos(3)
    marcar_como_falso(lista, 3)
    print(lista) # En consola: [True, True, True, False]
   ```

3. La función `es_verdadero` recibe como parámetros la lista `lista_booleanos` y el entero `indice`. Esta función
   retorna el elemento de índice `indice` en `lista_booleanos`.
   
   ```python
    lista = generar_lista_booleanos(3)
    marcar_como_falso(lista, 3)
    print(es_verdadero(lista, 3)) # En consola: False
   ```
4. La función `mostrar_verdaderos` recibe como parámetro la lista `lista_booleanos`. Esta función muestra en consola 
   los indices de elementos de `lista_booleanos` que tienen valor `True`, un índice por línea.
   
   ```python
    lista = generar_lista_booleanos(3)
    marcar_como_falso(lista, 3)
    mostrar_verdaderos(lista)
   # En consola:
   # 0
   # 1
   # 2
   ```
   
## Segunda Pregunta
Haciendo uso de las funciones definidas en la primera pregunta, muestre en consola todos **los numero primos 
entre 0 y 30**. Complete la función `iniciar` en `primos.py`, haciendo uso del siguiente algoritmo:

1. Utilize la función `generar_lista_booleanos` para generar una lista de booleanos, donde cada índice de la lista es 
   un candidato a primo. Un candidato a primo tiene como valor `True` en esta lista. Inicialmente, **todos** los índices 
   son candidatos a primo.
   
2. Empezando desde 2, descarte los indices que sean multiplos de un candidato a primo usando la función
   `marcar_como_falso` para asignarles el valor de `False`. 
   Por ejemplo, 4 al ser multiplo de dos **no** es un numero primo. 
   Para descartarlo, utilizamos `marcar_como_falso(4)`.
   Lo mismo se puede decir de 6, 8 y demás numeros pares.
   Realizamos este procedimiento para todos los siguientes candidatos a primo (3, 5, 7 ...).
   Podemos identificar si un indice corresponde a un candidato a primo mediante `es_verdadero`.
   
3. Una vez terminado, mostrar los candidatos a primo que no han sido descartados, mediante `mostrar_verdaderos`

La salida del programa debe tener el siguiente formato:

```commandline
2
3
5
7
11
13
17
19
23
29
```
## Tercera Pregunta

En la tercera pregunta, se requiere implementar un programa para mostrar listas en consola,
de acuerdo a un formato determinado.
Este programa **tiene** que hacer uso de las siguientes funciones, que usted debe definir en el archivo 
`tabla.py`: 

1. La función `mostrar_lista` recibe como parámetro una lista de listas. Esta función muestra en consola 
   la lista en un formato tabular, donde **cada columna tiene una longitud de 10 caracteres**.
   La primera fila contiene los índices de cada columna, precedidos por la letra `C`. 
   De manera análoga, la primera columna contiene los índices de cada fila, precedidos por la letra `F`.
   A mode ejemplo, el siguiente código:
      
   ```python
    lista_de_listas = [["a", "b", "c"],
                       [1, 2, 3],
                       [4.0, 5.0, 6.0]]
    mostrar_lista(lista_de_listas)
   ```
   
   Genera el siguiente texto en consola:

   ```commandline
             C0        C1        C2        
   F0        a         b         c         
   F1        1         2         3         
   F2        4.0       5.0       6.0       
   ```
2. La función `crear_lista` recibe como parámetros el entero `filas` y el entero `columnas`,
   y retorna una lista de listas.
   Esta lista contiene `filas` listas internas, y cada lista interna tiene `columnas`
   numeros enteros.
   En cada cada lista interna, los valores se incrementan de uno en uno, de izquierda a derecha.
   El primer elemento de cada lista interna es el último elemento de la lista anterior, más uno.
   Considere que el primer elemento de la primera lista interna es uno. A modo de ejemplo:
   
   ```python
   print(crear_lista(3, 4))
   # En consola:
   # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
   ```
   
3. Complete la función `iniciar`, para crear una lista de 10 filas y 10 columnas usando 
   la función `crear_lista` para luego mostrarla en consola mediante la función `mostrar_lista`.