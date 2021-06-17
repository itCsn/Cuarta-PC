# BIC01: Primera Práctica

## Primera Pregunta

Implemente un programa para determinar el **minimo** número de monedas a utilizar al momento 
de dar vuelto.
El programa debe realizar lo siguiente:

1. Solicite al usuario el ingreso del precio del producto a comprar, en centimos.
2. Muestra en pantalla el **minimo** número de monedas a utilizar al momento de dar el vuelto.

Asuma que el cliente paga con una moneda de 100 centimos, y que el precio del producto
siempre será menor o igual que 100 centimos.
Considere que solo se pueden usar monedas de 1, 5, 10 y 25 centimos.

La implementación debe realizarse en el archivo `vuelto.py`, entre las líneas marcadas como `#INICIO` y `#FIN`.
No remueva o modifique el código base.

Los mensajes en consola deben tener el siguiente formato:

```
Ingrese el precio en centimos: 28
Su vuelto es: 
2 monedas de 25 centimos
2 monedas de 10 centimos
2 monedas de 1 centimo
```

```
Ingrese el precio en centimos: 100
No hay vuelto
```

## Segunda Pregunta

Implemente un programa que muestre en pantalla **todas** las ternas pitagóricas cuyos valores sean menores o 
iguales a 20.

Una terna pitagórica es un conjunto ordenado de tres numeros enteros positivos, de modo que estos valores 
correspondan a la longitud de los lados de un triángulo recto.
De acuerdo al teorema de Pitágoras, dada una terna pitagórica `(a, b, c)` se cumple que a<sup>2</sup> +
b<sup>2</sup> = c<sup>2</sup>.

La implementación debe realizarse en el archivo `terna.py`, entre las líneas marcadas como `#INICIO` y `#FIN`.
No remueva o modifique el código base.

Los mensajes en consola deben tener el siguiente formato:

```
(3, 4, 5)
(5, 12, 13)
(6, 8, 10)
(8, 15, 17)
(9, 12, 15)
(12, 16, 20)
```

## Tercera Pregunta

Implemente un programa para convertir números del sistema binario al sistema decimal.
El programa debe realizar lo siguiente:

1. Solicite al usuario el ingreso de un número en sistema binario.
2. En caso el número ingresado sea un número binario válido, mostrar en pantalla el 
   equivalente del número en sistema decimal.
3. En caso el número ingresado en el paso 1 contenga digitos no válidos en el sistema 
   binario, mostrar un mensaje de error y solicitar el ingreso de un nuevo número.
   
Asuma que el usuario en el paso 1 solo ingresara números enteros. La implementación debe 
realizarse en el archivo `binario.py`, entre las líneas marcadas como `#INICIO` y `#FIN`.
No remueva o modifique el código base.

Los mensajes en consola deben tener el siguiente formato:

```
Ingrese un numero en sistema binario:11012
El numero ingresado no es valido.
Ingrese un numero en sistema binario:1101
El equivalente en decimal es 13
```
