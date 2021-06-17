# BIC01: Examen Parcial

## Primera Pregunta

Implemente un programa para generar las 52 cartas de una [baraja inglesa](https://es.wikipedia.org/wiki/Baraja_inglesa).
La baraja inglesa tiene cuatro palos (espadas, corazones, diamantes y tréboles) y cada palo está formado por 13
cartas (as, 2, 3, 4, 5, 6, 7, 8, 9, 10, jota, reina y rey). El programa debe realizar lo siguiente:

1. La baraja debe almacenarse en una lista de tuplas, donde cada tupla contiene el palo como primer elemento y la carta
   como segundo elemento, ambos representados mediante cadenas de caracteres. A modo de ejemplo, `print(baraja[:13])` podría
   mostrar lo siguiente en consola:

    ```commandline
    [('Espadas', 'As'), ('Espadas', 'Dos'), ('Espadas', 'Tres'), ('Espadas', 'Cuatro'), 
   ('Espadas', 'Cinco'), ('Espadas', 'Seis'), ('Espadas', 'Siete'), ('Espadas', 'Ocho'), 
   ('Espadas', 'Nueve'), ('Espadas', 'Diez'), ('Espadas', 'Jota'), ('Espadas', 'Reina'), 
   ('Espadas', 'Rey')]
    ```

3. Muestre en consola las cartas de la baraja en 4 columnas, donde cada columna tiene 20 caracteres de longitud. Las
   cartas deben mostrarse **en orden aleatorio**, luego de haber sido "barajeadas". A modo de ejemplo:

    ```commandline
   Seis de Corazones    Diez de Diamantes    Ocho de Treboles     Nueve de Espadas    
   As de Treboles       Nueve de Diamantes   Rey de Treboles      Dos de Corazones    
   Tres de Espadas      Diez de Treboles     Dos de Treboles      As de Corazones     
   Seis de Diamantes    Seis de Treboles     As de Diamantes      Reina de Diamantes  
   Cuatro de Diamantes  Ocho de Corazones    Jota de Corazones    Tres de Corazones   
   Jota de Espadas      Cuatro de Treboles   Nueve de Corazones   Siete de Treboles   
   Siete de Espadas     Rey de Espadas       Reina de Treboles    Dos de Espadas      
   Rey de Corazones     Rey de Diamantes     Ocho de Diamantes    Cinco de Espadas    
   Cuatro de Espadas    As de Espadas        Dos de Diamantes     Diez de Espadas     
   Siete de Corazones   Diez de Corazones    Cinco de Treboles    Ocho de Espadas     
   Tres de Treboles     Siete de Diamantes   Cuatro de Corazones  Cinco de Diamantes  
   Seis de Espadas      Reina de Espadas     Jota de Treboles     Reina de Corazones  
   Tres de Diamantes    Cinco de Corazones   Jota de Diamantes    Nueve de Treboles  
    ```
   
Para ordenar aleatoriamente una lista `baraja`, puede utilizar `random.shuffle(baraja)`. 
La implementación debe realizarse en el archivo `cartas.py`, entre las líneas marcadas como `#INICIO` y `#FIN`.
No remueva o modifique el código base.

## Segunda Pregunta

Implemente un programa para **ordenar y remover duplicados** de una lista de valores ingresados por el usuario.
El programa debe considerar lo siguiente:

1. Los elementos de la lista pueden ser o números enteros (`N`) o texto (`T`). El usuario debe indicar el tipo de elemento
   al inicio del programa.
   
2. El programa permite al usuario ingresar elementos a la lista. Para indicar que no hay más elementos pendientes, el 
   usuario debe ingresar `*` (asterisco).
   
3. En caso los elementos sean números enteros, los elementos deben mostrarse ordenados de menor a mayor valor, sin 
   considerar duplicados. 
   La salida en consola debe tener el siguiente formato:
   
   ```commandline
   Numeros (N) o texto (T)? N
   Ingrese un elemento de la lista (* para terminar): 1000
   Ingrese un elemento de la lista (* para terminar): 200
   Ingrese un elemento de la lista (* para terminar): 30
   Ingrese un elemento de la lista (* para terminar): 200
   Ingrese un elemento de la lista (* para terminar): 1000
   Ingrese un elemento de la lista (* para terminar): *
   Valores ingresados:
   *) 30
   *) 200
   *) 1000
   ```

4. En caso los elementos sean texto, los elementos deben mostrarse alfabéticamente, en orden ascendente, sin considerar 
   duplicados.
   La salida en consola debe tener el siguiente formato:

   ```commandline
   Numeros (N) o texto (T)? T
   Ingrese un elemento de la lista (* para terminar): BIC01
   Ingrese un elemento de la lista (* para terminar): W
   Ingrese un elemento de la lista (* para terminar): UNI
   Ingrese un elemento de la lista (* para terminar): FIIS
   Ingrese un elemento de la lista (* para terminar): W
   Ingrese un elemento de la lista (* para terminar): *
   Valores ingresados:
   *) BIC01
   *) FIIS
   *) UNI
   *) W
   ```
   
La implementación debe realizarse en el archivo `ordenar.py`, entre las líneas marcadas como `#INICIO` y `#FIN`.
No remueva o modifique el código base.

## Tercera Pregunta

Implemente un programa para el calcular el consumo de gasolina en multiples tramos.
El programa debe considerar lo siguiente:

1. Para cada tramo, los usuarios ingresan la cantidad de gasolina consumida (en galones) y la distancia 
   recorrida (en millas). Ambos valores son números reales. 
   Luego de ingresados ambos valores, el programa muestra en consola el consumo de gasolina para el tramo
   en millas con galón. El consumo es mostrado **redondeado a dos decimales**.
   
2. El programa permite al usuario ingresar múltiples tramos. Para indicar que no hay más tramos pendientes, el 
   usuario debe ingresar `-1` como consumo de gasolina para el tramo.
   
3. Luego de ingresados todos los tramos, el programa muestra en consola el número de tramos y el consumo total 
   de gasolina en millas por galón. El consumo es mostrado **redondeado a dos decimales**. 
   La salida en consola debe tener el siguiente formato:
   
   ```commandline
   Tramo 1: Ingrese la gasolina consumida, en galones (-1 para terminar): 12.8
   Tramo 1: Ingrese la distancia recorrida, en millas: 287
   En el tramo 1, el consumo de gasolina fue 22.42 millas por galon.
   Tramo 2: Ingrese la gasolina consumida, en galones (-1 para terminar): 10.3
   Tramo 2: Ingrese la distancia recorrida, en millas: 200
   En el tramo 2, el consumo de gasolina fue 19.42 millas por galon.
   Tramo 3: Ingrese la gasolina consumida, en galones (-1 para terminar): 5
   Tramo 3: Ingrese la distancia recorrida, en millas: 120
   En el tramo 3, el consumo de gasolina fue 24.0 millas por galon.
   Tramo 4: Ingrese la gasolina consumida, en galones (-1 para terminar): -1
   En 3 tramos, el consumo de gasolina fue 21.6 millas por galon.  
   ```

La implementación debe realizarse en el archivo `gasolina.py`, entre las líneas marcadas como `#INICIO` y `#FIN`.
No remueva o modifique el código base.